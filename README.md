# runkrate/.github

This repository holds the [**runkrate**](https://github.com/runkrate)
organization profile and shared GitHub configuration.

| Path | Purpose |
| ---- | ------- |
| [`profile/README.md`](profile/README.md) | Organization profile README (GitHub org landing page) |
| [`FUNDING.md`](FUNDING.md) | How to support / sponsor KRATE |
| [`FUNDING.yml`](FUNDING.yml) | Org-default GitHub Sponsor button (Ko-fi) |
| [`assets/logo/`](assets/logo/) | Shared KRATE logo assets |
| [`snippets/readme-header.md`](snippets/readme-header.md) | Shared visual README header (logo + badges) |
| [`snippets/readme-sync.json`](snippets/readme-sync.json) | Target repositories for header sync |
| [`scripts/sync_readme_header.py`](scripts/sync_readme_header.py) | Sync script (replace markers, open PRs) |

## Shared README header

Product READMEs include a synced block between:

```markdown
<!-- KRATE-README-HEADER:START -->
…
<!-- KRATE-README-HEADER:END -->
```

On changes to the header or logo, [`.github/workflows/sync-readme-header.yml`](.github/workflows/sync-readme-header.yml)
opens a PR on each target listed in `snippets/readme-sync.json`.

### Secret: `README_SYNC_TOKEN`

Create a fine-grained PAT (or GitHub App installation token) with:

- `contents: write`
- `pull_requests: write`

on organizations **`runkrate`** and **`krate-apps`** (all target repos).

Add it as a **repository secret** named `README_SYNC_TOKEN` on `runkrate/.github`.

Manual run: Actions → **Sync README header** → `workflow_dispatch` (optional `--seed` / dry-run inputs).
