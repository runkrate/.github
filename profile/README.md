<!-- KRATE-README-HEADER:START -->
<p align="center">
  <a href="https://github.com/runkrate">
    <img src="https://raw.githubusercontent.com/runkrate/.github/main/assets/logo/logo.png" alt="KRATE" width="128" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/runkrate/krate/stargazers"><img src="https://img.shields.io/github/stars/runkrate/krate?style=flat-square&logo=github" alt="GitHub stars" /></a>
  <a href="https://github.com/runkrate/krate/releases"><img src="https://img.shields.io/github/v/release/runkrate/krate?style=flat-square&label=version" alt="Current version" /></a>
  <a href="https://github.com/runkrate/krate/blob/main/LICENSE"><img src="https://img.shields.io/github/license/runkrate/krate?style=flat-square" alt="License" /></a>
</p>

<p align="center">
  <a href="https://runkrate.com"><img src="https://img.shields.io/badge/Website-runkrate.com-0A66C2?style=flat-square" alt="Website" /></a>
  <a href="https://runkrate.com/docs"><img src="https://img.shields.io/badge/Docs-runkrate.com%2Fdocs-111827?style=flat-square" alt="Docs" /></a>
  <a href="https://github.com/runkrate/hub/issues"><img src="https://img.shields.io/github/issues-search/runkrate/hub?query=is%3Aopen&style=flat-square&label=issues%2FPRs" alt="Open issues and pull requests" /></a>
</p>
<!-- KRATE-README-HEADER:END -->

# KRATE

**Unified Server and Application Management Platform**

KRATE transforms a standard Debian server into a fully managed ecosystem for media and automation stacks—including Jellyfin, the *arr suite, download clients, and associated services.

Engineered for simplicity and scale, KRATE provides everything required to operate your infrastructure from a single, cohesive environment. Administrate your system via **zen**, a highly responsive Command-Line Interface (CLI), or utilize **HarmonyUI** for comprehensive control through an intuitive web dashboard. Seamlessly manage applications, system services, user access, storage arrays, and updates without the overhead of maintaining disparate management tools.

**Deploy Once. Manage Centrally.**

*Official KRATE distributions are exclusively published via [`runkrate/krate`](https://github.com/runkrate/krate). All other organizational repositories contain source code, application catalogs, build infrastructure, and extensions; they do not serve as alternative installation endpoints.*

<br />

<p align="center">
  <a href="https://github.com/runkrate/krate#install"><strong>Install</strong></a>
  &nbsp;·&nbsp;
  <a href="https://runkrate.com/docs"><strong>Documentation</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/runkrate/krate/releases"><strong>Releases</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/runkrate/hub"><strong>Hub</strong></a>
</p>

<p align="center">
  <sub>Supported today: Debian&nbsp;13 (trixie), amd64 &nbsp;·&nbsp; Additional platforms planned</sub>
</p>

---

## System Requirements

| Requirement          | Specification                                                          |
| -------------------- | ---------------------------------------------------------------------- |
| **Operating System** | Debian 13 (Trixie)                                                     |
| **Architecture**     | amd64                                                                  |
| **Roadmap**          | Support for additional operating systems and architectures is planned. |

## Getting Started

For comprehensive installation procedures, please refer to the [installation guide within the `runkrate/krate` repository](https://github.com/runkrate/krate#install).

**Documentation:** [runkrate.com/docs](https://runkrate.com/docs)

## Issue Tracking & Contributions

Bug reports, feature requests, and project planning are centralized in **[Hub](https://github.com/runkrate/hub)**. Progress is tracked on the [organization project board](https://github.com/orgs/runkrate/projects).

Component repositories accept **pull requests** only. See the [Contributing Guidelines](https://github.com/runkrate/docs/blob/main/CONTRIBUTING.md).

## Project Architecture & Repositories

### Core Infrastructure

| Repository                                         | Description                                                           |
| -------------------------------------------------- | --------------------------------------------------------------------- |
| **[hub](https://github.com/runkrate/hub)**         | Centralized issue tracking, feature requests, and project planning    |
| **[krate](https://github.com/runkrate/krate)**     | Official release distribution (`.deb` packages, checksums, manifests) |
| **[console](https://github.com/runkrate/console)** | Source for the `zen` and `zenfw` CLI utilities                        |
| **[setup](https://github.com/runkrate/setup)**     | Source for the initial configuration wizard                           |
| **[web](https://github.com/runkrate/web)**         | Source for the HarmonyUI web interface                                |
| **[docs](https://github.com/runkrate/docs)**       | Source for the [official documentation](https://runkrate.com/docs)    |

### Application Catalogs

Application catalogs and related packages are maintained under **[krate-apps](https://github.com/krate-apps)**:

| Repository                                               | Description                                                      |
| -------------------------------------------------------- | ---------------------------------------------------------------- |
| [`core`](https://github.com/krate-apps/core)             | Official applications supported and maintained by the KRATE team |
| [`community`](https://github.com/krate-apps/community)   | Applications contributed and maintained by the community         |
| [`extensions`](https://github.com/krate-apps/extensions) | Optional third-party plugins and themes (e.g. ruTorrent)         |
| [`snapshots`](https://github.com/krate-apps/snapshots)   | Signed binary catalog and mirrored `.deb` packages               |

*Maintainer resources:* release automation at [`krate-tools/scripts`](https://github.com/krate-tools/scripts).

## Supporting KRATE

KRATE is primarily funded through its paid licenses. Optional one-time contributions are welcome on [Ko-fi](https://ko-fi.com/krate).

Details: [`FUNDING.md`](https://github.com/runkrate/.github/blob/main/FUNDING.md)

