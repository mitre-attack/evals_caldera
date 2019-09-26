# CALDERA plugin: Eval

## Overview

A plugin supplying CALDERA with the TTPs used within the ATT&CK Evaluations Round 1 (APT3).
For more information see https://attackevals.mitre.org/about-attack-evaluations.html

1. Plugin Installation
2. Lab Setup
3. Execution

## Installation
Clone the Eval plugin into the caldera/plugin directory
```commandline
git clone https://github.com/mitre/evals.git
```
Add Eval plugin to CALDERA config `conf/local.yml`
```yaml
plugins:
  - evals
```

Fill out facts in `data/facts/` specific to your setup.

## Environment Setup
[Full Round 1 Environment](https://attackevals.mitre.org/methodology/round1/environment.html)

Minimum requirements:
- Initial host exists within a windows domain
- Remote shared drive is mounted

## Execution

Please read the [full documentation](https://github.com/mitre/caldera/wiki/Plugins-evals) for this plugin.
