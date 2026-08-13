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

### Auth (Krate Release Bot)

CI mints GitHub App installation tokens via **Krate Release Bot**
(`KRATE_RELEASE_BOT_APP_ID` + `KRATE_RELEASE_BOT_PRIVATE_KEY` org secrets/vars on
**runkrate**). No separate `README_SYNC_TOKEN` PAT is required.

The app must be installed on **runkrate** and **krate-apps** with
`contents: write` and `pull_requests: write`.

Optional override: repository secret `README_SYNC_TOKEN` (single PAT for all targets).

Manual run: Actions → **Sync README header** → `workflow_dispatch` (optional seed / dry-run).
