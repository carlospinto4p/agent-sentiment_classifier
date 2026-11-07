"""Tests for the packaged agent: config, model, golden set, entry point.

No LLM calls. Run with `uv run pytest`.
"""

import json
from importlib.metadata import entry_points

import yaml
from agents7.agents import Classifier
from agents7.agents.utils import import_from_path

import sentiment_classifier
from sentiment_classifier import CONFIG_PATH, GOLDEN_SET_PATH
from sentiment_classifier.models import (
    Sentiment,
    SentimentCategory,
    SentimentReason,
)


def _config() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def _golden_rows() -> list[dict]:
    lines = GOLDEN_SET_PATH.read_text(encoding="utf-8").splitlines()
    return [json.loads(line) for line in lines if line.strip()]


# ── Config ──────────────────────────────────────────────────────


def test_config_ships_inside_the_package():
    assert CONFIG_PATH.is_file()
    assert GOLDEN_SET_PATH.is_file()


def test_output_model_resolves_to_the_package_model():
    assert import_from_path(_config()["output_model"]) is Sentiment


def test_config_builds_a_classifier():
    agent = Classifier.from_yaml(str(CONFIG_PATH))
    for category in SentimentCategory:
        assert category.name in agent.possible_categories
    assert "NOT_APPLICABLE" not in agent.possible_categories


def test_system_examples_are_valid_outputs():
    for example in _config()["system_examples"]:
        out = example["output"]
        category = SentimentCategory[out["category"]]
        reason = SentimentReason[out["reason"]]
        assert reason in Sentiment.CATEGORY_REASONS[category]


# ── Model ───────────────────────────────────────────────────────


def test_every_reason_belongs_to_exactly_one_category():
    listed = [r for rs in Sentiment.CATEGORY_REASONS.values() for r in rs]
    assert sorted(listed) == sorted(SentimentReason)


def test_not_applicable_is_disabled():
    assert Sentiment.NOT_APPLICABLE is False


# ── Golden set ──────────────────────────────────────────────────


def test_golden_set_rows_have_text_and_a_valid_category():
    rows = _golden_rows()
    assert rows
    for row in rows:
        assert row["text"]
        assert row["category"] in SentimentCategory.__members__


# ── Entry point ─────────────────────────────────────────────────


def test_entry_point_names_the_config():
    found = {ep.name: ep for ep in entry_points(group="agents7.agents")}
    assert "sentiment_classifier" in found
    assert found["sentiment_classifier"].load() == CONFIG_PATH
    assert found["sentiment_classifier"].module == (
        sentiment_classifier.__name__
    )
