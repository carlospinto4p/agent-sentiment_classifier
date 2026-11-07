# Sentiment Classifier

An LLM agent that labels a text as positive, negative or neutral, with a
reason for the label. Built with
[agents7](https://github.com/carlospinto4p/agents7), and run on Ollama
with `gemma3:12b` by default.

It is also the example of an agent packaged in its own repository, with
its own output model and eval set.

## Categories

| Category | Meaning | Reasons |
|----------|---------|---------|
| POSITIVE | Positive sentiment expressed | `ENTHUSIASTIC`, `GRATEFUL`, `HOPEFUL` |
| NEGATIVE | Negative sentiment expressed | `FRUSTRATED`, `DISAPPOINTED`, `ANGRY` |
| NEUTRAL | Neutral or objective tone | `FACTUAL`, `INFORMATIVE`, `DESCRIPTIVE` |

`NOT_APPLICABLE` is disabled: `NEUTRAL` already covers text with no
clear sentiment. The mapping lives in `CATEGORY_REASONS` on
`sentiment_classifier.models.Sentiment`.

## Install

The package is not on PyPI. Install a tagged release:

```bash
pip install "sentiment-classifier @ git+https://github.com/carlospinto4p/agent-sentiment_classifier@v0.1.2"
```

It depends on agents7 tag `v9.25.9`. Every package in one environment
must name the same agents7 tag.

## Usage

```python
from agents7.agents import Classifier

from sentiment_classifier import CONFIG_PATH

agent = Classifier.from_yaml(str(CONFIG_PATH))
response = agent.act({"text": "Best purchase ever!"})
print(response.model.category.name)  # POSITIVE
print(response.model.reason.name)    # ENTHUSIASTIC
```

## In agents7-ui

Install it into the UI backend's environment and
[agents7-ui](https://github.com/carlospinto4p/agents7-ui) lists it, with
its eval set. It is found through the `agents7.agents` entry point in
`pyproject.toml`.

## Evaluation

Run it against its golden set (9 rows, scored on `category`) with the
framework's `agents7 eval` command:

```bash
uv run agents7 eval \
    -c src/sentiment_classifier/config.yml \
    -d src/sentiment_classifier/data/golden_set.jsonl \
    -r reports/sentiment_classifier.md
```

`reports/` is git-ignored.

## Development

```bash
uv sync
uv run pytest
uv run ruff check src tests
```

The tests make no LLM calls.

The git history starts in the agents7 repository, where this agent
began as an example config.

## License

MIT
