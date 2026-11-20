# Agent specification template

## Context

Name the decision, the person who owns it, the trigger, and the point where the agent hands the work back. List the allowed output values. Give each authoritative source a stable ID, version and owner. Describe what happens when two sources disagree.

## Principles

Define the evidence required before a favourable decision. Identify which calculations must be deterministic, who can authorize any later action, and which inputs may contain untrusted instructions. Record one meaningful uncertainty the agent must communicate.

## Steps

| Step | Inputs needed | Decision or calculation | Evidence produced | Stop condition or next step |
| --- | --- | --- | --- | --- |
| Intake | | | | |
| Validate identity, authority and units | | | | |
| Evaluate | | | | |
| Explain and hand off | | | | |

## Rules and acceptance

| Rule ID | Exact condition, including equality | Output and reason | Source | Normal, boundary and failure case IDs |
| --- | --- | --- | --- | --- |
| | | | | |

Specify rule precedence, retry behaviour and the failure owner. Give every test an expected machine-readable result. Keep expected results separate from inputs when evaluating an agent. Record the version tested and any behaviour still requiring human review.
