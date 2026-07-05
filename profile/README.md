# KRATE

**Self-hosted media and automation for Linux servers.**

KRATE is a Debian-based stack that installs and runs media servers, *arr tools,
download clients, dashboards, and more — from a single command line (`zen`) and a
web interface (HarmonyUI). One package, one workflow: add users, deploy apps per
user, manage services, and keep everything up to date.

## Get started

Install the latest release:

```bash
curl -fsSL https://raw.githubusercontent.com/krate-client/krate/main/bootstrap.sh | sudo bash
```

Full guides: **[krate.github.io/docs](https://krate.github.io/docs/)**

## Bugs, ideas, and planning

All bug reports and feature requests go through **[hub](https://github.com/krate-client/hub)** — one place for the whole project, tracked on the [org project board](https://github.com/orgs/krate-client/projects).

Component repositories accept **pull requests** only; do not open issues there.

## Repositories

| Repository                                                             | What it is                                              |
| ---------------------------------------------------------------------- | ------------------------------------------------------- |
| [**hub**](https://github.com/krate-client/hub)                         | Bug reports, feature requests, and planning             |
| [**releases**](https://github.com/krate-client/krate)                  | Official `krate` `.deb` packages and release manifests  |
| [**web**](https://github.com/krate-client/web)                         | HarmonyUI — the web dashboard                           |
| [**apps-official**](https://github.com/krate-client/apps-official)     | Official application catalog (public, read-only mirror) |
| [**apps-community**](https://github.com/krate-client/apps-community)   | Community-contributed applications                      |
| [**apps-extensions**](https://github.com/krate-client/apps-extensions) | Optional add-ons and plugins for KRATE applications     |
| [**docs**](https://github.com/krate-client/docs)                       | User-facing documentation sources                       |

## How apps work

Applications are folders with metadata (`meta.yaml`, `manifest.yaml`) and a
lifecycle handler. KRATE ships two catalogs — **official** and **community** —
inside the `krate` package. Before running any handler, `zen` verifies its
SHA-256 checksum and RSA signature against the signed `CATALOG.json` bundled with
your installation.

## Links

- Website & docs: [krate.github.io](https://krate.github.io/)
- Documentation: [krate.github.io/docs](https://krate.github.io/docs/)
- Releases: [github.com/krate-client/krate](https://github.com/krate-client/krate/releases)

---

*This organization hosts the open-source client side of KRATE.*
