import streamlit as st
from collections import Counter
from src.utils.data import (
    load_text,
    parse_results,
    get_all_values,
)
from src.utils.show_reviews import show_reviews

REVIEWS_PATH = "data/reviews_sample.txt"
KEYPHRAES_PATH = "data/keyphrases.txt"

st.set_page_config(
    page_title="Key phrases in hotel reviews",
    page_icon="🏨",
)


def init() -> tuple[list[str], dict]:
    reviews = load_text(REVIEWS_PATH)
    key_phrases = load_text(KEYPHRAES_PATH, is_json=True)
    return reviews, parse_results(key_phrases, "KeyPhrases")


st.markdown("# Key phrases in reviews")

reviews, key_phrases = init()
unique_phrases = Counter(get_all_values(key_phrases, "Text"))

st.sidebar.subheader("Info")
st.sidebar.text(f"Reviews number: {len(reviews)}")
st.sidebar.text(f"Unique key phrases: {len(unique_phrases)}")

show_reviews(reviews=reviews, annotations=key_phrases)
