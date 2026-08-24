import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Product Review Sentiment Analyzer")

@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

st.title("Product Review Sentiment Analyzer")

review = st.text_area("Enter a product review")

if st.button("Analyze") and review.strip():
    model = load_model()
    result = model(review, truncation=True)[0]

    sentiment = "Positive" if "POSITIVE" in result["label"].upper() else "Negative"

    st.write("Sentiment:", sentiment)
    st.write("Confidence:", round(float(result["score"]), 4))
