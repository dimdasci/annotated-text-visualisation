import streamlit as st

st.set_page_config(
    page_title="Hotel reviews",
    page_icon="🏨",
)

st.write("# Opinion Extraction Methods")

st.markdown(
    """
    Dataset [La Veranda Hotel reviews on Booking.com](\
    https://www.kaggle.com/datasets/michelhatab/hotel-reviews-bookingcom)

    The project demonstrates the results of the following method 
    for identifying opinions and their polarity in hotel reviews:
    - AWS Comprehend pre-trained key phrases extraction,
    - AWS Comprehend targeted sentiment extraction,
    - [PyABSA](https://github.com/yangheng95/PyABSA) pre-trained aspect 
    term extraction and aspect term polarity classification.
    
    While Comprehend provide us with terms extraction feature only, 
    PyABSA solves both extraction and polarity classification tasks.

    Moreover, PyABSA provides two options of solving the task:
    1. aspect term extraction and polarity classification (ATEPC) 
    with a single model
    1. aspect terms extraction (ATE) and aspect polarity classification (APC)
    in two steps with two different models.

"""
)
