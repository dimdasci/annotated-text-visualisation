import streamlit as st
from annotated_text import annotated_text
from collections import Counter
from src.utils.data import (
    load_text,
    parse_results,
    get_all_phrases,
    make_annotations,
)

st.set_page_config(
    page_title="Entities in hotel reviews",
    page_icon="🏨",
)

REVIEWS_PATH = "data/reviews.csv"
ENTITIES_PATH = "data/entities.txt"


def init() -> tuple[list[str], dict]:
    reviews = load_text(REVIEWS_PATH)
    entities = load_text(ENTITIES_PATH, is_json=True)
    return reviews, parse_results(entities, "Entities")


st.markdown("# Entities")

reviews, entities = init()
unique_entities = Counter(get_all_phrases(entities))

st.sidebar.subheader("Info")
st.sidebar.text(f"# Reviews: {len(reviews)}")
st.sidebar.text(f"Unique entities: {len(unique_entities)}")
st.sidebar.write(unique_entities)

for i, r in enumerate(reviews[:15]):
    st.header(f"#{i:3d}")
    annotated_review = (
        make_annotations(r, entities[i]) if i in entities else [r]
    )
    annotated_text(*annotated_review)
