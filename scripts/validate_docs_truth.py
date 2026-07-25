#!/usr/bin/env python3
"""Validate public documentation claims against the canonical skill files."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

PUBLIC_BASE = "https://nevitonsantana.github.io/adaptive-skills"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def skill_category(path: Path) -> str | None:
    text = path.read_text()
    match = re.search(r"^metadata:\s*$.*?^\s{2}category:\s*['\"]?([^\n'\"]+)", text, re.M | re.S)
    return match.group(1).strip() if match else None


def catalog_index_names(text: str) -> list[str]:
    return re.findall(
        r"^\| (?:\[)?`([a-z0-9-]+)`(?:\]\([^)]+\))? \|",
        text,
        re.M,
    )


def frontmatter_value(text: str, field: str) -> str | None:
    match = re.search(rf"^{re.escape(field)}:\s*['\"]?([^\n'\"]+)", text, re.M)
    return match.group(1).strip() if match else None


def metadata_value(text: str, field: str) -> str | None:
    match = re.search(
        rf"^metadata:\s*$.*?^\s{{2}}{re.escape(field)}:\s*['\"]?([^\n'\"]+)",
        text,
        re.M | re.S,
    )
    return match.group(1).strip() if match else None


def detail_registry(root: Path, errors: list[str]) -> list[dict[str, str]]:
    path = root / "docs" / "skills" / "registry.json"
    try:
        data = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"docs/skills/registry.json: cannot read valid JSON: {error}")
        return []

    entries = data.get("skills") if isinstance(data, dict) else None
    if not isinstance(entries, list) or not entries:
        errors.append("docs/skills/registry.json: skills must be a non-empty array")
        return []

    normalized: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, entry in enumerate(entries):
        source = f"docs/skills/registry.json: skills[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{source}: entry must be an object")
            continue
        skill_id = entry.get("id")
        title = entry.get("title")
        if not isinstance(skill_id, str) or not re.fullmatch(r"[a-z0-9-]+", skill_id):
            errors.append(f"{source}: id must be a lowercase skill slug")
            continue
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{source}: title must be a non-empty string")
            continue
        if skill_id in seen:
            errors.append(f"docs/skills/registry.json: duplicate skill id {skill_id}")
            continue
        seen.add(skill_id)
        normalized.append({"id": skill_id, "title": title.strip()})
    return normalized


def category_rosters(text: str) -> dict[str, set[str]]:
    rosters: dict[str, set[str]] = {}
    sections = re.split(r'^## ', text, flags=re.M)[1:]
    for section in sections:
        name, _, body = section.partition('\n')
        published = re.search(r'^- \*\*Published:\*\* (.+)$', body, re.M)
        if published:
            rosters[name.strip()] = set(re.findall(r'`([a-z0-9-]+)`', published.group(1)))
    return rosters


def main() -> int:
    root = repo_root()
    skills: dict[str, str] = {}
    errors: list[str] = []

    for path in sorted(root.glob('skills/*/SKILL.md')):
        category = skill_category(path)
        if not category:
            errors.append(f'{path.relative_to(root)}: missing metadata.category')
            continue
        skills[path.parent.name] = category

    catalog_path = root / 'docs/getting-started/skill-catalog.md'
    catalog_text = catalog_path.read_text()
    catalog_names = catalog_index_names(catalog_text)
    duplicates = sorted(name for name, count in Counter(catalog_names).items() if count > 1)
    if duplicates:
        errors.append(f'catalog index contains duplicate skills: {", ".join(duplicates)}')
    missing = sorted(set(skills) - set(catalog_names))
    unknown = sorted(set(catalog_names) - set(skills))
    if missing:
        errors.append(f'catalog index is missing skills: {", ".join(missing)}')
    if unknown:
        errors.append(f'catalog index contains unknown skills: {", ".join(unknown)}')

    canonical_by_category: dict[str, set[str]] = defaultdict(set)
    for name, category in skills.items():
        canonical_by_category[category].add(name)

    category_path = root / 'docs/skill-categories.md'
    documented_by_category = category_rosters(category_path.read_text())
    for category in sorted(set(canonical_by_category) | set(documented_by_category)):
        canonical = canonical_by_category.get(category, set())
        documented = documented_by_category.get(category, set())
        if canonical != documented:
            missing_names = sorted(canonical - documented)
            unknown_names = sorted(documented - canonical)
            detail: list[str] = []
            if missing_names:
                detail.append(f'missing {", ".join(missing_names)}')
            if unknown_names:
                detail.append(f'unknown {", ".join(unknown_names)}')
            errors.append(f'category {category}: {"; ".join(detail)}')

    registry = detail_registry(root, errors)
    registered_ids = {entry["id"] for entry in registry}
    index_path = root / "docs" / "skills" / "index.md"
    index_text = index_path.read_text() if index_path.exists() else ""
    if not index_text:
        errors.append("docs/skills/index.md: missing public skill reference index")

    for entry in registry:
        skill_id = entry["id"]
        canonical_path = root / "skills" / skill_id / "SKILL.md"
        if not canonical_path.exists():
            errors.append(
                f"docs/skills/registry.json: unknown canonical skill {skill_id}"
            )
            continue

        canonical_text = canonical_path.read_text()
        required_values = {
            "name": frontmatter_value(canonical_text, "name"),
            "description": frontmatter_value(canonical_text, "description"),
            "metadata.version": metadata_value(canonical_text, "version"),
            "metadata.owner": metadata_value(canonical_text, "owner"),
            "metadata.category": metadata_value(canonical_text, "category"),
        }
        for field, value in required_values.items():
            if not value:
                errors.append(f"{canonical_path.relative_to(root)}: missing {field}")
        if required_values["name"] and required_values["name"] != skill_id:
            errors.append(
                f"{canonical_path.relative_to(root)}: name does not match registry id {skill_id}"
            )

        detail_url = f"{PUBLIC_BASE}/skills/{skill_id}/"
        expected_link = f"[`{skill_id}`]({detail_url})"
        if expected_link not in catalog_text:
            errors.append(
                f"docs/getting-started/skill-catalog.md: missing detail link for {skill_id}"
            )
        if expected_link not in index_text:
            errors.append(f"docs/skills/index.md: missing detail link for {skill_id}")

    linked_detail_ids = set(
        re.findall(
            rf"{re.escape(PUBLIC_BASE)}/skills/([a-z0-9-]+)/",
            catalog_text,
        )
    )
    unknown_detail_links = sorted(linked_detail_ids - registered_ids)
    if unknown_detail_links:
        errors.append(
            "catalog links unregistered skill detail pages: "
            + ", ".join(unknown_detail_links)
        )

    if errors:
        print('Documentation truth validation failed:')
        for error in errors:
            print(f'- {error}')
        return 1

    print(
        f"Validated public catalog and category coverage for {len(skills)} canonical "
        f"skills, including {len(registry)} registered detail profiles."
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
