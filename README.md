# Sentiment Classifier

An LLM agent that labels a text as positive, negative or neutral, with a
reason for the label. Built with
[agents7](https://github.com/carlospinto4p/agents7); it needs an LLM
backend (Ollama with `gemma3:12b` by default).

It is also the worked example of an agent kept in a repository of its
own: it carries its own output model, its own eval set, and declares
itself to tools that list installed agents.

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
pip install "sentiment-classifier @ git+https://github.com/carlospinto4p/sentiment_classifier@v0.1.0"
```

It depends on a tagged release of agents7. Every package installed in
one environment must name the same agents7 tag.

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

The package declares an entry point in the `agents7.agents` group:

```toml
[project.entry-points."agents7.agents"]
sentiment_classifier = "sentiment_classifier:CONFIG_PATH"
```

Install it into the UI backend's environment and the UI lists it, with
its eval set, without any catalog folder.

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

The tests make no LLM calls: they check the config, the model, the
golden set and the entry point.

## History

This agent started as a config in the agents7 framework repository
(`examples/configs/demo_sentiment_classifier.yml`, then
`samples/sentiment_classifier/`). Its history here is that file's
history, carried over.

## License

MIT
