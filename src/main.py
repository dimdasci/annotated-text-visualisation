import streamlit as st

st.set_page_config(
    page_title="Hotel reviews",
    page_icon="🏨",
)

st.write("# Hotel Reviews analysis")

st.markdown(
    """
    Dataset [La Veranda Hotel reviews on Booking.com](\
    https://www.kaggle.com/datasets/michelhatab/hotel-reviews-bookingcom)

    For each review you can explore key phrases and entities extracted with
    AWS Comprehend.
"""
)
