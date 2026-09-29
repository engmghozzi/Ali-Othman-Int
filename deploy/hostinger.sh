#!/usr/bin/env bash
set -euo pipefail
# No delete, clean, mirror, DNS or database operations are permitted here.
: "${HOSTINGER_HOST:?}" "${HOSTINGER_PORT:?}" "${HOSTINGER_USER:?}" "${HOSTINGER_ROOT:?}"
[[ "$HOSTINGER_HOST" =~ ^[a-zA-Z0-9.-]+$ ]]
[[ "$HOSTINGER_PORT" =~ ^[0-9]+$ ]]
[[ "$HOSTINGER_USER" =~ ^[a-zA-Z0-9_-]+$ ]]
[[ "$HOSTINGER_ROOT" =~ ^/home/[a-zA-Z0-9_/-]+/public_html$ ]]
[[ "$HOSTINGER_ROOT" != *..* ]]
target="$HOSTINGER_USER@$HOSTINGER_HOST"
ssh_options=(-p "$HOSTINGER_PORT" -o BatchMode=yes -o StrictHostKeyChecking=yes)
release="${GITHUB_RUN_ID:?}-${GITHUB_RUN_ATTEMPT:?}"
backup="${HOSTINGER_ROOT%/public_html}/company-site-backups/$release"
paths=(assets ar en ao-website.css site.js index.html)
# Validate the actual root and every destination path before writing anything.
# Existing symlinks are rejected, including links inside the three website folders.
ssh "${ssh_options[@]}" "$target" bash -s -- "$HOSTINGER_ROOT" "$backup" <<'REMOTE'
set -euo pipefail
root="$1"
backup="$2"
test -d "$root"
test "$(realpath "$root")" = "$root"
command -v rsync >/dev/null
for item in assets ar en ao-website.css site.js index.html; do
  path="$root/$item"
  test ! -L "$path"
  if test -d "$path"; then
    test -z "$(find "$path" -type l -print -quit)"
  fi
done
mkdir -p "$backup"
test "$(realpath "$backup")" = "$backup"
REMOTE
export RSYNC_RSH="ssh -p $HOSTINGER_PORT -o BatchMode=yes -o StrictHostKeyChecking=yes"
for item in "${paths[@]}"; do
  test -e "dist/$item"
  test ! -L "dist/$item"
  # Without a source trailing slash, rsync merges each named folder into root.
  rsync -rt --delay-updates --backup --backup-dir="$backup" \
    "dist/$item" "$target:$HOSTINGER_ROOT/"
done
printf 'Uploaded website files. Previous replaced files: %s\n' "$backup"
