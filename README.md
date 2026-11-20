# Agent Build Playbook
Malachi Pride · 255 Networks

A reviewer has one purchase order, one invoice and a decision to make. This playbook shows how to turn a short operating procedure into bounded agent instructions and testable outcomes.

## Start here

1. Read [the fictional operating procedure](procedure.md). It is the policy authority for this example.
2. Compare it with [the completed agent specification](worked-spec.md). Each rule points to a decision, an evidence requirement and an acceptance case.
3. Use [the blank template](agent-template.md) on a different procedure.
4. Run `python3 -m unittest -v` from this directory. Python 3.10+ and its standard library are sufficient.

The sample invoice of USD 1,021 exceeds a USD 1,000 order by USD 21. The applicable tolerance is USD 20, so the agent returns REVIEW even though the variance is less than USD 25.

## What the tests establish

[acceptance.json](acceptance.json) is a machine-readable set of fictional records with expected decisions and reasons. [reference_decision.py](reference_decision.py) is an independent deterministic interpretation of the worked spec. To evaluate another agent, present only the input field to the agent and compare its response with the expected fields. The included checks exercise the reference function. They do not measure a language model's accuracy.
