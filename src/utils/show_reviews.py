import streamlit as st
from annotated_text import annotated_text
from src.utils.paginator import paginator
from src.utils.data import make_annotations
from src.utils.pyabs_data import make_annotations as make_annotations_abs


def show_reviews(reviews: list, annotations: dict) -> None:
    for i, r in paginator(
        "Select a review page", reviews, items_per_page=25, on_sidebar=False
    ):
        st.header(f"#{i:03d}")
        annotated_review = (
            make_annotations(r, annotations[i]) if i in annotations else [r]
        )
        annotated_text(*annotated_review)


def show_reviews_abs(reviews: list) -> None:
    classifier = st.radio(
        "Classifier: two-step APC or a single step ATEPC", ["APC", "ATEPC"]
    )
    for i, r in paginator(
        "Select a review page", reviews, items_per_page=25, on_sidebar=False
    ):
        st.header(f"#{i:03d}")
        annotated_review = make_annotations_abs(r, kind=classifier.lower())
        annotated_text(*annotated_review)
