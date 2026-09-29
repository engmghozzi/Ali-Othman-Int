# Hostinger deployment setup

The workflow is manual only (GitHub Actions → Deploy company website to Hostinger).
It is not operational until the environment below is configured and the first
deployment is verified. No push triggers production deployment.

Create a GitHub environment named `hostinger-production` with:

Variables:
- `HOSTINGER_HOST`: hosting SSH address from hPanel.
- `HOSTINGER_PORT`: hosting SSH port from hPanel.
- `HOSTINGER_USER`: hosting SSH username from hPanel.
- `HOSTINGER_ROOT`: verified absolute main-domain public_html path, obtained on
  the server. Do not guess this value from the file-manager display.

Secrets:
- `HOSTINGER_SSH_KEY`: dedicated deployment private key, never committed.
- `HOSTINGER_KNOWN_HOSTS`: SSH host key verified against a trusted server
  fingerprint. Do not bypass host-key verification or blindly trust ssh-keyscan.

Authorize the corresponding public key in Hostinger only after the owner approves
its access scope. A normal account SSH key can access the account's other systems;
the script's allowlist limits its operations but does not restrict the credential.

The server requires bash, realpath, find, and rsync. The script refuses symlinked
targets, merges only the six approved website entries, and never uses --delete.
It backs up replaced files outside public_html in company-site-backups/run-attempt.
It does not provide a site-wide atomic switch; a short mixed-version interval is
possible while pages upload. After deployment verify Arabic and English pages,
images, PDFs, form markup, and all four subdomain systems. Do not send test forms
or claim mailbox delivery without checking activation and actual receipt.

For rollback, copy only the affected website files from the run's backup after
reviewing them. New files from that release may remain; do not run a broad cleanup
or restore the entire hosting account. Retain backups until validation completes.
