import { createHash } from "node:crypto";
import { existsSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { join, posix } from "node:path";
import { fileURLToPath } from "node:url";

import matter from "blume/core/frontmatter";
import type { ContentSource, SourceEntry } from "blume/sources/types";

interface SkillRegistryEntry {
  id: string;
  title: string;
}

interface SkillRegistry {
  skills: SkillRegistryEntry[];
}

interface SkillMetadata {
  category: string;
  owner: string;
  version: string;
}

const repoRoot = fileURLToPath(new URL("../..", import.meta.url));
const registryPath = join(repoRoot, "docs", "skills", "registry.json");
const skillsRoot = join(repoRoot, "skills");
const sourceBodies = new Map<string, string>();

const canonicalUrl = (id: string): string =>
  `https://github.com/nevitonsantana/adaptive-skills/blob/main/skills/${id}/SKILL.md`;

const editUrl = (id: string): string =>
  `https://github.com/nevitonsantana/adaptive-skills/edit/main/skills/${id}/SKILL.md`;

const requireString = (
  value: unknown,
  field: string,
  source: string
): string => {
  if (typeof value !== "string" || value.trim() === "") {
    throw new Error(`${source}: missing or invalid ${field}`);
  }
  return value.trim();
};

const parseRegistry = async (): Promise<SkillRegistryEntry[]> => {
  const source = await readFile(registryPath, "utf-8");
  const parsed = JSON.parse(source) as Partial<SkillRegistry>;
  if (!Array.isArray(parsed.skills) || parsed.skills.length === 0) {
    throw new Error(
      "docs/skills/registry.json: skills must be a non-empty array"
    );
  }

  const seen = new Set<string>();
  return parsed.skills.map((entry, index) => {
    const sourceName = `docs/skills/registry.json: skills[${index}]`;
    const id = requireString(entry?.id, "id", sourceName);
    const title = requireString(entry?.title, "title", sourceName);
    if (!/^[a-z0-9-]+$/u.test(id)) {
      throw new Error(`${sourceName}: id must be a lowercase skill slug`);
    }
    if (seen.has(id)) {
      throw new Error(`docs/skills/registry.json: duplicate skill id ${id}`);
    }
    seen.add(id);
    return { id, title };
  });
};

const rewriteRelativeLinks = (line: string, id: string): string =>
  line.replace(/\]\(([^)]+)\)/gu, (match, rawTarget: string) => {
    const target = rawTarget.trim();
    if (
      target.startsWith("#") ||
      target.startsWith("/") ||
      /^[a-z][a-z0-9+.-]*:/iu.test(target)
    ) {
      return match;
    }

    const [pathAndQuery, ...titleParts] = target.split(/\s+(?=["'])/u);
    const [pathWithQuery, fragment = ""] = pathAndQuery.split("#", 2);
    const [path, query = ""] = pathWithQuery.split("?", 2);
    const repositoryPath = posix.normalize(posix.join("skills", id, path));
    const suffix = [
      query ? `?${query}` : "",
      fragment ? `#${fragment}` : "",
      titleParts.length > 0 ? ` ${titleParts.join(" ")}` : "",
    ].join("");

    const aletheiaPrefix = "../aletheia/";
    if (repositoryPath.startsWith(aletheiaPrefix)) {
      const aletheiaPath = repositoryPath.slice(aletheiaPrefix.length);
      return `](https://github.com/nevitonsantana/AletheIA/blob/main/${aletheiaPath}${suffix})`;
    }
    if (repositoryPath.startsWith("../")) {
      throw new Error(
        `skills/${id}/SKILL.md: relative link escapes the repository: ${target}`
      );
    }

    return `](https://github.com/nevitonsantana/adaptive-skills/blob/main/${repositoryPath}${suffix})`;
  });

const renderContract = (source: string, id: string): string => {
  const lines = source.split("\n");
  let fenceCharacter: "`" | "~" | undefined;
  let fenceLength = 0;

  return lines
    .map((line) => {
      const fence = line.match(/^\s*(`{3,}|~{3,})/u)?.[1];
      if (fence) {
        const character = fence[0] as "`" | "~";
        if (!fenceCharacter) {
          fenceCharacter = character;
          fenceLength = fence.length;
        } else if (
          character === fenceCharacter &&
          fence.length >= fenceLength
        ) {
          fenceCharacter = undefined;
          fenceLength = 0;
        }
        return line;
      }

      if (!fenceCharacter && line.startsWith("# ")) {
        return rewriteRelativeLinks(`#${line}`, id);
      }
      return fenceCharacter ? line : rewriteRelativeLinks(line, id);
    })
    .join("\n");
};

const parseSkill = async (
  registryEntry: SkillRegistryEntry
): Promise<SourceEntry> => {
  const relativePath = `skills/${registryEntry.id}/SKILL.md`;
  const path = join(repoRoot, relativePath);
  const source = await readFile(path, "utf-8");
  const parsed = matter(source);

  const name = requireString(parsed.data.name, "name", relativePath);
  if (name !== registryEntry.id) {
    throw new Error(
      `${relativePath}: frontmatter name ${name} does not match registry id ${registryEntry.id}`
    );
  }
  const description = requireString(
    parsed.data.description,
    "description",
    relativePath
  );
  const metadataValue = parsed.data.metadata;
  if (
    typeof metadataValue !== "object" ||
    metadataValue === null ||
    Array.isArray(metadataValue)
  ) {
    throw new Error(`${relativePath}: missing or invalid metadata`);
  }
  const metadataRecord = metadataValue as Record<string, unknown>;
  const metadata: SkillMetadata = {
    category: requireString(
      metadataRecord.category,
      "metadata.category",
      relativePath
    ),
    owner: requireString(metadataRecord.owner, "metadata.owner", relativePath),
    version: requireString(
      metadataRecord.version,
      "metadata.version",
      relativePath
    ),
  };

  const body = [
    "> **Canonical skill profile.** This page is generated from the repository contract. The linked `SKILL.md` remains the source of authority.",
    "",
    "| Category | Version | Owner |",
    "|---|---|---|",
    `| \`${metadata.category}\` | \`${metadata.version}\` | \`${metadata.owner}\` |`,
    "",
    "## Jump to",
    "",
    "- [Overview](#overview)",
    "- [When to use](#when-to-use)",
    "- [When not to use](#when-not-to-use)",
    "- [Core moves](#core-moves)",
    "- [Expected output](#expected-output)",
    "- [Verification](#verification)",
    "- [Handoff signals](#handoff-signals)",
    "- [Pairs well with](#pairs-well-with)",
    "- [Anti-patterns](#anti-patterns)",
    "",
    `[View the canonical contract on GitHub](${canonicalUrl(registryEntry.id)}).`,
    "",
    renderContract(parsed.content.trim(), registryEntry.id),
    "",
  ].join("\n");
  const data = {
    description,
    title: registryEntry.title,
  };
  const raw = [
    "---",
    `title: ${JSON.stringify(registryEntry.title)}`,
    `description: ${JSON.stringify(description)}`,
    "---",
    "",
    body,
  ].join("\n");
  const ref = `${registryEntry.id}.md`;
  sourceBodies.set(ref, body);

  return {
    body: { format: "md", text: body },
    data,
    editUrl: editUrl(registryEntry.id),
    hash: createHash("sha256").update(raw).digest("hex"),
    raw,
    ref,
    slug: registryEntry.id,
  };
};

export const skillReferenceSource: ContentSource = {
  name: "skill-reference",
  prefix: "skills",
  staged: true,
  load: async () => {
    sourceBodies.clear();
    const registry = await parseRegistry();
    const entries = await Promise.all(registry.map(parseSkill));
    return { diagnostics: [], entries };
  },
  read: async (ref) => sourceBodies.get(ref) ?? "",
  validate: () => {
    if (!existsSync(registryPath)) {
      throw new Error(
        "Skill reference registry not found: docs/skills/registry.json"
      );
    }
    if (!existsSync(skillsRoot)) {
      throw new Error("Canonical skills directory not found: skills/");
    }
  },
};
