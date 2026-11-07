# Changelog


### v0.1.1 - 7th November 2026

- The repository is renamed to `agent-sentiment_classifier`, so agent
  repositories share a prefix. `README.md` installs from the new URL.
  The package name is unchanged.


### v0.1.0 - 7th November 2026

- Moved out of the agents7 framework's `samples/sentiment_classifier/`
  into a repository of its own, keeping that config's history.
- Added the package `sentiment_classifier`:
  - `models.py`: `Sentiment`, `SentimentCategory`, `SentimentReason`,
    copied from `agents7.models.demo`.
  - `config.yml`: the agent config, now resolving its output model
    from this package.
  - `data/golden_set.jsonl`: the 9-row eval set.
  - `CONFIG_PATH`, named by an `agents7.agents` entry point.
- Depends on agents7 tag `v9.25.9`.
- Added `tests/test_package.py`: 8 tests, no LLM calls.
- MIT licence.
