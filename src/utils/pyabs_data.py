import json

COLORS = {"Positive": "#B9EACF", "Neutral": "#E5E5E5", "Negative": "#FBD3E0"}


def load_results(aspects_path: str, sentiments_path: str) -> list:
    results = []
    # reviews = []

    with open(aspects_path, "r", encoding="utf-8") as f:
        aspects = json.load(f)
    with open(sentiments_path, "r", encoding="utf-8") as f:
        sentiments = json.load(f)

    idx = 0
    for row in aspects:
        record = {
            "sentence_ate": row["sentence"],
            "tokens_ate": row["tokens"],
            "aspect_ate": row["aspect"],
            "position_ate": row["position"],
            "sentiment_ate": row["sentiment"],
            "confidence_ate": row["confidence"],
        }

        if len(row["aspect"]) > 0:
            # get sentiments from APC
            record["sentence_apc"] = sentiments[idx]["text"]
            record["aspect_apc"] = sentiments[idx]["aspect"]
            record["sentiment_apc"] = sentiments[idx]["sentiment"]
            record["confidence_apc"] = sentiments[idx]["confidence"]
            idx += 1
        results.append(record)

    return results


def make_annotations(record: dict, kind: str = "apc") -> list:
    annotated_text = []
    suffix = "_apc" if kind == "apc" else "_ate"
    last_position = 0

    for i, aspect in enumerate(record["aspect_ate"]):
        sentiment = record[f"sentiment{suffix}"][i]
        confidence = record[f"confidence{suffix}"][i]
        position = record["position_ate"][i][0] - 1
        color = COLORS.get(sentiment, "#F00")
        annotated_text.append(
            " ".join(record["tokens_ate"][last_position:position])
        )
        annotated_text.append((aspect, sentiment, color))
        last_position = position + len(aspect.split())

    if last_position < len(record["tokens_ate"]) - 1:
        annotated_text.append(" ".join(record["tokens_ate"][last_position:]))

    return annotated_text
