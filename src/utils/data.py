"""
Module for managing AWS Comprehend data
"""
import streamlit as st
import json

COLORS = {"Positive": "#B9EACF", "Neutral": "#E5E5E5", "Negative": "#FBD3E0"}


def dequote(text: str) -> str:
    result = text.strip()
    if result[0] == '"' and result[-1] == '"':
        result = f" {text[1:-2]}"

    return result


def load_text(filename: str, is_json: bool = False) -> list:
    data = []
    parse_fn = json.loads if is_json else dequote
    with open(file=filename) as file:
        data = [parse_fn(_) for _ in file]
    return data


def parse_results(data: list[dict], key: str) -> dict:
    return {line["Line"]: line[key] for line in data if len(line[key]) > 0}


def make_annotations(
    text: str, phrases: list, is_entity: bool = False
) -> list:
    result = []
    if is_entity:
        mentions = sorted(
            [mention for p in phrases for mention in p["Mentions"]],
            key=lambda item: item.get("BeginOffset", 0),
        )
    else:
        mentions = phrases

    last_position = 0
    for entry in mentions:
        substring = text[last_position : entry["BeginOffset"]]
        annotated = text[entry["BeginOffset"] : entry["EndOffset"]]

        if "MentionSentiment" in entry:
            sentiment = entry["MentionSentiment"]["Sentiment"].capitalize()
        else:
            sentiment = "Neutral"
        color = COLORS.get(sentiment, "#F00")

        last_position = entry["EndOffset"]
        result.append(substring)
        result.append((annotated, entry.get("Type", "Key"), color))
    if last_position < len(text) - 1:
        result.append(text[last_position:])
    return result


def get_all_values(data: dict, key: str) -> list[str]:
    return [item[key] for entries in data.values() for item in entries]
