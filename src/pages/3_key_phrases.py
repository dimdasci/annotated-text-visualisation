import streamlit as st
from src.utils.data import load_text, parse_results
import numpy as np
import pandas as pd

KEYPHRAES_PATH = "data/keyphrases.txt"
STOP_WORDS = ["the", "a", "all"]


def clear_text(text: str) -> str:
    result = text.lower()
    result = " ".join(
        [word for word in result.split() if word not in STOP_WORDS]
    )
    return result


def aggregate(data: dict) -> list[list]:
    interim = {}
    result = []
    KEY = "Text"

    for items in data.values():
        for item in items:
            phrase = clear_text(item[KEY])
            if phrase in interim:
                interim[phrase].append(item["Score"])
            else:
                interim[phrase] = [item["Score"]]

    for phrase, scores in interim.items():
        result.append([phrase, len(scores), np.mean(scores), np.std(scores)])

    return pd.DataFrame(
        result, columns=["phrase", "number", "score_mean", "score_std"]
    )


key_phrases = parse_results(
    load_text(KEYPHRAES_PATH, is_json=True), "KeyPhrases"
)
phrases_df = aggregate(data=key_phrases)

max_number = int(phrases_df.number.max())

st.markdown("# Key phrases")
st.subheader("Filters")
number_range = st.slider(
    "Number of occurrences",
    min_value=1,
    max_value=max_number,
    value=[1, max_number],
)
score_range = st.slider(
    "Mean score", min_value=0.0, max_value=1.0, value=[0.0, 1.0], step=0.05
)

filtered_df = phrases_df[
    phrases_df.number.between(number_range[0], number_range[1])
    & phrases_df.score_mean.between(score_range[0], score_range[1])
]
st.text(f"Found {filtered_df.shape[0]} phrases")

st.subheader("Data")
st.dataframe(
    filtered_df,
    use_container_width=True,
)
