# KRATE

**Self-hosted media and automation for Linux servers.**

KRATE is a Debian-based stack that installs and runs media servers, *arr tools,
download clients, dashboards, and more — from a single command line (`zen`) and a
web interface (HarmonyUI). One package, one workflow: add users, deploy apps per
user, manage services, and keep everything up to date.

## Get started

Install the latest release:

```bash
curl -fsSL https://raw.githubusercontent.com/runkrate/krate/main/bootstrap.sh | sudo bash
```

Full guides: **[runkrate/docs](https://github.com/runkrate/docs)**

## Bugs, ideas, and planning

All bug reports and feature requests go through **[hub](https://github.com/runkrate/hub)** — one place for the whole project, tracked on the [org project board](https://github.com/orgs/runkrate/projects).

Component repositories accept **pull requests** only; do not open issues there.

## Repositories

| Repository                                                         | What it is                                              |
| ------------------------------------------------------------------ | ------------------------------------------------------- |
| [**hub**](https://github.com/runkrate/hub)                         | Bug reports, feature requests, and planning             |
| [**krate**](https://github.com/runkrate/krate)                     | Official `krate` `.deb` packages and release manifests  |
| [**console**](https://github.com/runkrate/console)                 | `zen` / `zenfw` CLI and runtime                         |
| [**setup**](https://github.com/runkrate/setup)                     | First-install wizard                                    |
| [**web**](https://github.com/runkrate/web)                         | HarmonyUI — the web dashboard                           |
| [**docs**](https://github.com/runkrate/docs)                       | User-facing documentation sources                       |
| [**sentinel**](https://github.com/runkrate/sentinel)               | GitHub → Discord activity bot (Cloudflare Workers)      |

Application catalogs and binary packages live in sibling orgs:

| Organization / repo                                                    | What it is                                              |
| ---------------------------------------------------------------------- | ------------------------------------------------------- |
| [`krate-apps/sources`](https://github.com/krate-apps/sources)          | Official app handlers (authoring; encrypted publish)    |
| [`krate-apps/core`](https://github.com/krate-apps/core)                | Official apps mirror (public / package catalog)         |
| [`krate-apps/community`](https://github.com/krate-apps/community)      | Community-contributed applications                      |
| [`krate-apps/extensions`](https://github.com/krate-apps/extensions)    | Optional add-ons and plugins                            |
| [`krate-apps/snapshots`](https://github.com/krate-apps/snapshots)      | Signed `BINARIES_CATALOG.json` + mirrored `.deb`s       |
| [`krate-tools/scripts`](https://github.com/krate-tools/scripts)        | Release CI tooling (`.deb` build, catalog, GitHub helpers) |

## How apps work

Applications are folders with metadata (`meta.yaml`, `manifest.yaml`) and a
lifecycle handler. KRATE ships two catalogs — **official** and **community** —
inside the `krate` package. Before running any handler, `zen` verifies its
SHA-256 checksum and RSA signature against the signed `CATALOG.json` bundled with
your installation.

## Links

- Documentation: [github.com/runkrate/docs](https://github.com/runkrate/docs)
- Releases: [github.com/runkrate/krate](https://github.com/runkrate/krate/releases)

---

*This organization hosts the open-source KRATE client stack and related product repos.*
