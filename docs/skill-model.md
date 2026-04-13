# Skill Model

## Why this model exists

Rigid step-by-step skills break when one skill supports multiple task shapes.
Unstructured skills break because they depend on improvisation.

Adaptative Skills uses a middle path:

- **Core Moves** for invariants
- **Optional Modules** for context-specific depth
- **Activation Triggers** for lightweight adaptiveness

## Core Moves

`Core Moves` are the few actions that should almost always happen.

Rules:
- 3 to 5 moves
- durable over time
- easy to scan quickly
- not a full procedure tree

## Optional Modules

Modules are contextual blocks.

Examples:
- risk review
- stakeholder alignment
- coverage gap analysis
- accessibility lens

Modules do not turn on by default.

## Activation Triggers

Triggers are natural-language cues such as:
- if the change is high-risk
- if the work crosses multiple functions
- if an existing interface already exists
- if another system consumes the contract

They are not a mini policy engine.

## Sidecars

A skill folder may include:
- `templates/`
- `checklists/`
- `examples/`
- `references/`
- `changelog.md`

Only add them when they reduce cognitive load or improve reuse.

## What not to do

- do not make the core a giant checklist
- do not create modules for one-off edge cases
- do not create empty sidecar folders
- do not turn a skill into a mini framework
