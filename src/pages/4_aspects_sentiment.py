import streamlit as st
from src.utils.pyabs_data import load_results
from src.utils.show_reviews import show_reviews_abs

st.set_page_config(
    page_title="Aspect sentiments in hotel reviews",
    page_icon="🏨",
)

ASPECTS_SENTIMENT_PATH = "data/sentiments.json"
ASPECTS_PATH = "data/atepc_inference.result.json"

reviews = load_results(
    aspects_path=ASPECTS_PATH, sentiments_path=ASPECTS_SENTIMENT_PATH
)

st.markdown("# Aspect sentiments in reviews")


st.sidebar.subheader("Info")
st.sidebar.text(f"# Reviews: {len(reviews)}")

show_reviews_abs(reviews=reviews)
