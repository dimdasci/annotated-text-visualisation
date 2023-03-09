import streamlit as st
from annotated_text import annotated_text
from collections import Counter
from src.utils.data import (
    load_text,
    parse_results,
    get_all_phrases,
    make_annotations,
)

REVIEWS_PATH = "data/reviews.csv"
KEYPHRAES_PATH = "data/keyphrases.txt"

st.set_page_config(
    page_title="Key phrases in hotel reviews",
    page_icon="🏨",
)


def init() -> tuple[list[str], dict]:
    reviews = load_text(REVIEWS_PATH)
    key_phrases = load_text(KEYPHRAES_PATH, is_json=True)
    return reviews, parse_results(key_phrases, "KeyPhrases")


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
