from enum import StrEnum
from typing import ClassVar

from agents7.models import ClassificationProperty


class SentimentCategory(StrEnum):
    """Categories for sentiment classification."""

    POSITIVE = "Positive sentiment expressed."
    NEGATIVE = "Negative sentiment expressed."
    NEUTRAL = "Neutral or objective tone."


class SentimentReason(StrEnum):
    """Reasons justifying the sentiment classification."""

    # Positive reasons
    ENTHUSIASTIC = "Expresses enthusiasm or excitement."
    GRATEFUL = "Shows gratitude or appreciation."
    HOPEFUL = "Conveys hope or optimism."
    # Negative reasons
    FRUSTRATED = "Expresses frustration or annoyance."
    DISAPPOINTED = "Shows disappointment or sadness."
    ANGRY = "Conveys anger or hostility."
    # Neutral reasons
    FACTUAL = "Primarily factual, objective tone."
    INFORMATIVE = "Provides information without emotion."
    DESCRIPTIVE = "Describes without judgment."


class Sentiment(ClassificationProperty):
    """Sentiment of a text: a category plus the reason for it.

    NOT_APPLICABLE is disabled because the NEUTRAL category
    already covers texts with no clear sentiment.
    """

    NOT_APPLICABLE = False

    category: SentimentCategory
    reason: SentimentReason

    CATEGORY_REASONS: ClassVar[dict[StrEnum, list[StrEnum]]] = {
        SentimentCategory.POSITIVE: [
            SentimentReason.ENTHUSIASTIC,
            SentimentReason.GRATEFUL,
            SentimentReason.HOPEFUL,
        ],
        SentimentCategory.NEGATIVE: [
            SentimentReason.FRUSTRATED,
            SentimentReason.DISAPPOINTED,
            SentimentReason.ANGRY,
        ],
        SentimentCategory.NEUTRAL: [
            SentimentReason.FACTUAL,
            SentimentReason.INFORMATIVE,
            SentimentReason.DESCRIPTIVE,
        ],
    }
