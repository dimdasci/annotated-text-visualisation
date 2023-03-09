import streamlit as st
from collections import Counter
from src.utils.data import (
    load_text,
    parse_results,
    get_all_values,
)
from src.utils.show_reviews import show_reviews

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


st.markdown("# Entities in reviews")

reviews, entities = init()
unique_entities = Counter(get_all_values(entities, "Text"))
unique_types = Counter(get_all_values(entities, "Type"))

st.sidebar.subheader("Info")
st.sidebar.text(f"# Reviews: {len(reviews)}")
st.sidebar.text(f"# Unique entities: {len(unique_entities)}")
st.sidebar.text(f"# Unique entity types: {len(unique_types)}")
st.sidebar.write(unique_types)

show_reviews(reviews=reviews, annotations=entities)
