import streamlit as st
from annotated_text import annotated_text
from collections import Counter

import json

REVIEWS_PATH = "data/reviews.csv"
KEYPHRAES_PATH = "data/keyphrases.txt"

st.set_page_config(
    page_title="Key phrases in hotel reviews",
    page_icon="🏨",
)

def load_text(filename: str, is_json: bool = False) -> list:
    data = []
    parse_fn = (lambda s: json.loads(s)) if is_json else (lambda s: s)
    with open(file=filename) as file:
        data = [parse_fn(_) for _ in file]
    return data

def parse_key_phrases(data: list[dict]) -> dict:
    return { line["Line"] : line["KeyPhrases"] for line in data if len(line["KeyPhrases"]) > 0}

def init() -> tuple[list[str], dict]:
    reviews = load_text(REVIEWS_PATH)
    key_phrases = load_text(KEYPHRAES_PATH, is_json=True)
    return reviews, parse_key_phrases(key_phrases)

def make_annotations(text: str, phrases: list) -> list:
    result = []
    last_position = 0
    for entry in phrases:
        substring = text[last_position: entry["BeginOffset"]]
        annotated = text[entry["BeginOffset"]: entry["EndOffset"]]
        last_position = entry["EndOffset"]
        result.append(substring)
        result.append((annotated, "key"))
    if last_position < len(text)-1:
        result.append(text[last_position:])
    return result

def get_all_phrases(phrases: dict) -> list[str]:
    return [item["Text"] for entries in phrases.values() for item in entries]

st.markdown("# Key phrases")

reviews, key_phrases = init()
unique_phrases = Counter(get_all_phrases(key_phrases))

st.sidebar.subheader("Info")
st.sidebar.text(f"Reviews number: {len(reviews)}")
st.sidebar.text(f"Unique key phrases: {len(unique_phrases)}")
st.sidebar.write(unique_phrases)

for i, r in enumerate(reviews[:15]):
    st.header(f"#{i:3d}")
    annotated_review = make_annotations(r, key_phrases[i])
    annotated_text(*annotated_review)
