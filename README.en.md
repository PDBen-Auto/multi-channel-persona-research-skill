# Multi-Channel Persona Research Skill

Turn authorized reviews, community discussions, support summaries, and product behavior into traceable behavioral personas. Use those personas to screen product or experience variants and design a real A/B test.

## Problem

Single-source summaries overrepresent vocal users. Static personas often lack behavioral evidence. AI-simulated votes can be mistaken for measured click or conversion rates. This Skill connects source records, channel bias, behavioral segments, variant hypotheses, and experiment design while preserving unknowns.

## Workflow

`complementary sources -> deduplicated evidence -> behavioral segments -> blinded variant review -> pre-specified A/B test`

The package is industry-agnostic and instruction-only. It can reduce early discovery and screening effort, but it does not replace representative research or randomized experiment results.

## Install

```bash
npx skills add PDBen-Auto/multi-channel-persona-research-skill --skill multi-channel-persona-research
```

Invoke with `$multi-channel-persona-research`. Provide a decision question, target scope, authorized evidence, and optional variants. Offline analysis of supplied material needs no account or proprietary API; live collection may require permitted access and platform-specific tools.

## Example and boundaries

The [fully synthetic appointment-onboarding case](references/synthetic-case.md) demonstrates six invented observations, two behavioral hypotheses, a blinded variant comparison, and a proposed randomized test. It contains no real users, source URLs, or measured win rate.

See [README.md](README.md) for the full Chinese guide, inputs, outputs, differentiation, and licensing. The Skill does not perform identity enrichment, collect contacts, infer sensitive traits, or turn simulated preferences into actual conversion statistics.
