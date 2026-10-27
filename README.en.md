# Multi-Channel Persona Research Skill

Turn authorized reviews, community discussions, support summaries, and product behavior into traceable behavioral personas. Use those personas to screen product or experience variants and design a real A/B test. This workflow applies to software, physical products, services, and content experiences.

## Problem it solves

Early product decisions often need to be made before interviews or surveys are available. Single-source summaries overrepresent vocal users; static personas often lack behavioral evidence; AI-simulated votes can be mistaken for measured click or conversion rates. This Skill creates a low-cost path for early discovery and variant screening. It does not replace representative research or a randomized experiment.

## What makes it different

| Common approach | This Skill |
| --- | --- |
| Summarize one channel | Combine complementary channels and record each channel's sampling bias. |
| Describe a fictional average user | Segment by task, trigger, current workaround, friction, and choice criteria. |
| Ask AI personas to vote on variants | Use evidence for directional screening; never invent segment weights or win rates. |
| Decide test metrics after launch | Pre-specify randomization unit, primary metric, guardrails, segments, and decision rule. |

Workflow: `complementary sources -> deduplicated evidence -> behavioral segments -> blinded variant review -> pre-specified A/B test`. A conclusion can be traced back to a source record, and an experiment hypothesis can be traced back to a persona judgment. Missing evidence remains `unknown`.

## Who it is for

Product managers, researchers, growth teams, independent builders, and commerce or service operators with some authorized customer evidence but limited early research capacity.

## Install

```bash
npx skills add PDBen-Auto/multi-channel-persona-research-skill --skill multi-channel-persona-research
```

Invoke with `$multi-channel-persona-research`. For example: "Use authorized support summaries, app reviews, and forum discussions to build behavioral personas for a booking tool. Mark source, date, channel bias, and unknowns; compare two blinded onboarding variants and propose a real A/B test."

Offline analysis of supplied material needs no account, proprietary API, or paid data source. Live collection depends on channel access, authorization, and platform rules; restricted sources are skipped rather than bypassed. The repository contains no crawler, user records, or tracking callback.

## Inputs and outputs

**Inputs:** A decision question, target user and context, at least one authorized source, and optional variants. Claims of cross-channel corroboration require at least two independent source types. Unknown baselines, population weights, and coverage stay unknown.

**Outputs:** A source ledger, de-identified evidence records, behavior-based persona hypotheses, a variant-fit matrix, and a conditional A/B test brief. The default report can be `persona-research.md`; structured tables can be requested. No personal records are published automatically.

## Synthetic example

The [fully synthetic appointment-onboarding case](references/synthetic-case.md) demonstrates six invented observations across three source types, two behavioral hypotheses, a blinded variant comparison, and a proposed randomized test with a seven-day first-success metric. It contains no real users, source URLs, or measured win rate.

## Boundaries

Public reviews and community posts are convenience samples and cannot establish market share. The Skill does not perform cross-platform identity matching, collect contacts, infer sensitive traits, or turn simulated preferences into conversion statistics. With only one channel or weak evidence, it returns limited hypotheses and gaps rather than a verified persona. High-stakes investment decisions need direct user research and real behavior validation.

## Ecosystem and license

Use [Amazon Review Intelligence](https://github.com/PDBen-Auto/amazon-review-intelligence-skill) to collect and preserve written Amazon reviews, then this Skill to combine authorized customer signals across channels. Use [Amazon Product Research Agent Skills](https://github.com/PDBen-Auto/amazon-product-research-agent-skills) for broader product evidence and investment gates. These adjacent workflows do not remove this Skill's sampling or experiment limits.

See [README.md](README.md) for the full Chinese guide and [LICENSE](LICENSE) for terms: installation and use of the unmodified package are allowed; modification, redistribution, and product embedding require separate permission.
