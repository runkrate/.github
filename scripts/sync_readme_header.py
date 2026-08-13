#!/usr/bin/env python3
"""Sync the shared KRATE README header into target repositories and open PRs.

Usage:
  python3 scripts/sync_readme_header.py [--dry-run] [--seed]
  python3 scripts/sync_readme_header.py --apply-file /path/to/README.md [--seed]

Environment:
  README_SYNC_TOKEN_RUNKRATE / README_SYNC_TOKEN_KRATE_APPS — preferred (GitHub App
    installation tokens per org).
  README_SYNC_TOKEN or GH_TOKEN / GITHUB_TOKEN — single-token fallback.
  GITHUB_SHA (optional) — source commit referenced in PR bodies.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "snippets" / "readme-sync.json"

START_DEFAULT = "<!-- KRATE-README-HEADER:START -->"
END_DEFAULT = "<!-- KRATE-README-HEADER:END -->"


def load_config() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def read_header(config: dict) -> str:
    header_path = ROOT / config["header_file"]
    return header_path.read_text(encoding="utf-8").strip() + "\n"


def apply_header(
    readme: str,
    header: str,
    start: str,
    end: str,
    *,
    seed: bool,
) -> str:
    inner = f"{start}\n{header.rstrip()}\n{end}"
    if start in readme and end in readme:
        pattern = re.compile(
            re.escape(start) + r".*?" + re.escape(end),
            re.DOTALL,
        )
        updated, n = pattern.subn(inner, readme, count=1)
        if n != 1:
            raise RuntimeError("failed to replace existing header markers")
        return updated

    if not seed:
        raise RuntimeError(
            "README is missing KRATE-README-HEADER markers "
            "(use --seed to insert them at the top)"
        )

    body = readme.lstrip("\n")
    return f"{inner}\n\n{body}" if body else f"{inner}\n"


def run(
    cmd: list[str],
    *,
    cwd: Path | None = None,
    env: dict | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    merged = os.environ.copy()
    if env:
        merged.update(env)
    return subprocess.run(
        cmd,
        cwd=cwd,
        env=merged,
        text=True,
        capture_output=True,
        check=check,
    )


def token_for(owner: str) -> str:
    """Resolve a write token for the target org (App tokens preferred)."""
    owner_key = owner.strip().upper().replace("-", "_")
    for key in (
        f"README_SYNC_TOKEN_{owner_key}",
        "README_SYNC_TOKEN",
        "GH_TOKEN",
        "GITHUB_TOKEN",
    ):
        value = os.environ.get(key, "").strip()
        if value:
            return value
    raise SystemExit(
        f"Missing token for owner={owner}: set README_SYNC_TOKEN_{owner_key} "
        "(or README_SYNC_TOKEN / GH_TOKEN / GITHUB_TOKEN)"
    )


def token() -> str:
    """Legacy single-token helper (local --apply-file does not need it)."""
    for key in ("README_SYNC_TOKEN", "GH_TOKEN", "GITHUB_TOKEN"):
        value = os.environ.get(key, "").strip()
        if value:
            return value
    # Prefer any org-scoped token if present
    for key, value in os.environ.items():
        if key.startswith("README_SYNC_TOKEN_") and value.strip():
            return value.strip()
    raise SystemExit(
        "Missing token: set README_SYNC_TOKEN_RUNKRATE / README_SYNC_TOKEN_KRATE_APPS "
        "(or README_SYNC_TOKEN / GH_TOKEN / GITHUB_TOKEN)"
    )


def gh_env(tok: str) -> dict[str, str]:
    return {"GH_TOKEN": tok, "GITHUB_TOKEN": tok}


def sync_target(
    target: dict,
    header: str,
    start: str,
    end: str,
    *,
    seed: bool,
    dry_run: bool,
    tok: str,
    source_sha: str,
) -> None:
    owner = target["owner"]
    repo = target["repo"]
    branch = target["branch"]
    path = target.get("path", "README.md")
    full = f"{owner}/{repo}"
    print(f"==> {full} ({branch}:{path})")

    with tempfile.TemporaryDirectory(prefix="krate-readme-sync-") as tmp:
        work = Path(tmp) / repo
        clone_url = f"https://x-access-token:{tok}@github.com/{full}.git"
        run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                branch,
                clone_url,
                str(work),
            ],
            env=gh_env(tok),
        )
        # Keep the tokenized origin URL for later push (do not scrub to bare https).

        readme_path = work / path
        if not readme_path.is_file():
            raise RuntimeError(f"{full}: {path} not found")

        original = readme_path.read_text(encoding="utf-8")
        updated = apply_header(original, header, start, end, seed=seed)
        if updated == original:
            print("    unchanged")
            return

        if dry_run:
            print(
                f"    dry-run: would update {path} "
                f"({len(original)} → {len(updated)} bytes)"
            )
            return

        readme_path.write_text(updated, encoding="utf-8")
        head_branch = "chore/sync-readme-header"
        run(["git", "checkout", "-B", head_branch], cwd=work)
        run(
            ["git", "config", "user.name", "krate-release-bot[bot]"],
            cwd=work,
        )
        run(
            [
                "git",
                "config",
                "user.email",
                "4030630+krate-release-bot[bot]@users.noreply.github.com",
            ],
            cwd=work,
        )
        run(["git", "add", path], cwd=work)
        status = run(["git", "status", "--porcelain"], cwd=work, check=False)
        if not status.stdout.strip():
            print("    no diff after write")
            return

        msg = "chore(readme): sync shared KRATE header"
        run(["git", "commit", "-m", msg], cwd=work)
        run(
            ["git", "push", "-u", "origin", "HEAD", "--force"],
            cwd=work,
            env=gh_env(tok),
        )

        existing = run(
            [
                "gh",
                "pr",
                "list",
                "--repo",
                full,
                "--head",
                head_branch,
                "--base",
                branch,
                "--json",
                "url",
                "--jq",
                ".[0].url // empty",
            ],
            cwd=work,
            env=gh_env(tok),
            check=False,
        )
        if existing.stdout.strip():
            print(f"    updated PR {existing.stdout.strip()}")
            return

        body = (
            "## Summary\n"
            "- Sync shared visual README header (logo + badges) from "
            "[`runkrate/.github`](https://github.com/runkrate/.github).\n"
        )
        if source_sha:
            body += (
                f"- Source commit: [`{source_sha[:7]}`]"
                f"(https://github.com/runkrate/.github/commit/{source_sha})\n"
            )
        body += (
            "\nThis PR only updates the block between "
            "`KRATE-README-HEADER` markers.\n"
        )
        created = run(
            [
                "gh",
                "pr",
                "create",
                "--repo",
                full,
                "--base",
                branch,
                "--head",
                head_branch,
                "--title",
                msg,
                "--body",
                body,
            ],
            cwd=work,
            env=gh_env(tok),
        )
        print(f"    opened {created.stdout.strip()}")


def apply_local_file(
    path: Path,
    header: str,
    start: str,
    end: str,
    *,
    seed: bool,
) -> None:
    original = path.read_text(encoding="utf-8")
    updated = apply_header(original, header, start, end, seed=seed)
    if updated == original:
        print(f"unchanged: {path}")
        return
    path.write_text(updated, encoding="utf-8")
    print(f"updated: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not push or open PRs",
    )
    parser.add_argument(
        "--seed",
        action="store_true",
        help="Insert markers at top of README when missing",
    )
    parser.add_argument(
        "--apply-file",
        type=Path,
        help="Apply header to a local README path only (no git/PR)",
    )
    args = parser.parse_args()

    config = load_config()
    start = config.get("marker_start", START_DEFAULT)
    end = config.get("marker_end", END_DEFAULT)
    header = read_header(config)

    if args.apply_file:
        apply_local_file(args.apply_file, header, start, end, seed=args.seed)
        return 0

    source_sha = os.environ.get("GITHUB_SHA", "").strip()
    errors: list[str] = []

    for target in config["targets"]:
        try:
            sync_target(
                target,
                header,
                start,
                end,
                seed=args.seed,
                dry_run=args.dry_run,
                tok=token_for(target["owner"]),
                source_sha=source_sha,
            )
        except Exception as exc:  # noqa: BLE001 — collect per-target failures
            msg = f"{target['owner']}/{target['repo']}: {exc}"
            print(f"ERROR: {msg}", file=sys.stderr)
            if isinstance(exc, subprocess.CalledProcessError):
                err = (exc.stderr or exc.stdout or "").strip()
                if err:
                    print(err, file=sys.stderr)
            errors.append(msg)

    if errors:
        print(f"\n{len(errors)} target(s) failed", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
