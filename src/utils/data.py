"""
Module for managing data
"""

import json


def load_text(filename: str, is_json: bool = False) -> list:
    data = []
    parse_fn = (lambda s: json.loads(s)) if is_json else (lambda s: s)
    with open(file=filename) as file:
        data = [parse_fn(_) for _ in file]
    return data


def parse_results(data: list[dict], key: str) -> dict:
    return {line["Line"]: line[key] for line in data if len(line[key]) > 0}


def make_annotations(text: str, phrases: list) -> list:
    result = []
    last_position = 0
    for entry in phrases:
        substring = text[last_position : entry["BeginOffset"]]
        annotated = text[entry["BeginOffset"] : entry["EndOffset"]]
        last_position = entry["EndOffset"]
        result.append(substring)
        result.append((annotated, entry.get("Type", "Key")))
    if last_position < len(text) - 1:
        result.append(text[last_position:])
    return result


def get_all_phrases(phrases: dict) -> list[str]:
    return [item["Text"] for entries in phrases.values() for item in entries]
