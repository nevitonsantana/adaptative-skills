#!/usr/bin/env python3
"""Validate the rendered Blume documentation quality baseline."""
from __future__ import annotations

import json
import re
import posixpath
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    dist = root / "apps" / "docs" / "dist"
    errors: list[str] = []
    pages = sorted(dist.rglob("index.html"))

    if not pages:
        print("Rendered documentation validation failed:")
        print("- no index.html pages found; run the documentation build first")
        return 1

    registry_path = root / "docs" / "skills" / "registry.json"
    try:
        registry = json.loads(registry_path.read_text())
        registered_ids = [
            entry["id"]
            for entry in registry["skills"]
            if isinstance(entry, dict) and isinstance(entry.get("id"), str)
        ]
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as error:
        print("Rendered documentation validation failed:")
        print(f"- cannot read skill detail registry: {error}")
        return 1

    for page in pages:
        text = page.read_text(errors="ignore")
        relative = page.relative_to(dist)
        h1_count = len(re.findall(r"<h1(?:\s|>)", text))
        if h1_count != 1:
            errors.append(f"{relative}: expected exactly one visible H1, found {h1_count}")

        heading_levels = [int(level) for level in re.findall(r"<h([1-6])(?:\s|>)", text)]
        for previous, current in zip(heading_levels, heading_levels[1:]):
            if current > previous + 1:
                errors.append(
                    f"{relative}: heading hierarchy jumps from H{previous} to H{current}"
                )
                break

        for href in re.findall(r'href="([^"]+)"', text):
            parsed = urlparse(href)
            same_public_site = (
                parsed.netloc == "nevitonsantana.github.io"
                and parsed.path.startswith("/adaptive-skills")
            )
            if (parsed.scheme or parsed.netloc) and not same_public_site:
                continue
            if not parsed.path:
                continue
            target = parsed.path
            if target.lower().endswith((".md", ".mdx")):
                errors.append(f"{relative}: local link opens Markdown instead of a rendered route: {href}")
                continue

            if target.startswith("/adaptive-skills/"):
                site_path = target.removeprefix("/adaptive-skills/")
            elif target == "/adaptive-skills":
                site_path = ""
            elif target.startswith("/"):
                errors.append(f"{relative}: root link escapes the GitHub Pages base path: {href}")
                continue
            else:
                page_route = relative.parent.as_posix()
                site_path = posixpath.normpath(posixpath.join(page_route, target))

            candidate = dist / site_path
            if not (candidate.is_file() or (candidate / "index.html").is_file()):
                errors.append(f"{relative}: local link does not resolve to a published route: {href}")

    skill_index = dist / "skills" / "index.html"
    if not skill_index.exists():
        errors.append("skills/index.html: missing rendered skill reference index")

    required_section_ids = {
        "overview",
        "when-to-use",
        "when-not-to-use",
        "core-moves",
        "optional-modules",
        "activation-triggers",
        "expected-output",
        "verification",
        "handoff-signals",
        "pairs-well-with",
        "anti-patterns",
    }
    for skill_id in registered_ids:
        relative = Path("skills") / skill_id / "index.html"
        page = dist / relative
        if not page.exists():
            errors.append(f"{relative}: missing rendered registered skill profile")
            continue
        text = page.read_text(errors="ignore")
        heading_ids = set(re.findall(r'<h[1-6][^>]* id="([^"]+)"', text))
        missing_sections = sorted(required_section_ids - heading_ids)
        if missing_sections:
            errors.append(
                f"{relative}: missing canonical sections: {', '.join(missing_sections)}"
            )
        canonical_url = (
            "https://github.com/nevitonsantana/adaptive-skills/blob/main/"
            f"skills/{skill_id}/SKILL.md"
        )
        if canonical_url not in text:
            errors.append(f"{relative}: missing canonical SKILL.md source link")

        canonical_text = (
            root / "skills" / skill_id / "SKILL.md"
        ).read_text(errors="ignore")
        for target in re.findall(
            r"\]\(\.\./\.\./\.\./aletheia/([^)]+)\)",
            canonical_text,
        ):
            expected_url = (
                "https://github.com/nevitonsantana/AletheIA/blob/main/"
                f"{target}"
            )
            if expected_url not in text:
                errors.append(
                    f"{relative}: missing rewritten AletheIA source link: "
                    f"{expected_url}"
                )

    if errors:
        print("Rendered documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validated {len(pages)} rendered documentation pages, including "
        f"{len(registered_ids)} canonical skill profiles: one H1 each, continuous "
        "heading hierarchy, valid published local routes, and complete skill sections."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
