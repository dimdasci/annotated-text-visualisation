import streamlit as st
from annotated_text import annotated_text
from src.utils.paginator import paginator
from src.utils.data import make_annotations


def show_reviews(reviews: list, annotations: dict) -> None:
    for i, r in paginator(
        "Select a review page", reviews, items_per_page=50, on_sidebar=False
    ):
        st.header(f"#{i:3d}")
        annotated_review = (
            make_annotations(r, annotations[i]) if i in annotations else [r]
        )
        annotated_text(*annotated_review)
