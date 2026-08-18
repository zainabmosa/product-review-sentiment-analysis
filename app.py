import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Product Review Sentiment", page_icon="🛍️")

st.title("🛍️ Product Review Sentiment Analyzer")
st.write("Enter a product review and a pretrained Hugging Face model will classify its sentiment.")

MODEL_OPTIONS = {
    "DistilBERT SST-2": "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    "NLP Town Product Reviews": "nlptown/bert-base-multilingual-uncased-sentiment",
    "CardiffNLP RoBERTa": "cardiffnlp/twitter-roberta-base-sentiment-latest",
}

@st.cache_resource
def load_model(model_id):
    return pipeline("text-classification", model=model_id)

model_name = st.selectbox("Choose a pretrained model", list(MODEL_OPTIONS.keys()))
review = st.text_area(
    "Product review",
    placeholder="Example: The product is excellent and works perfectly!"
)

if st.button("Analyze Review"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        classifier = load_model(MODEL_OPTIONS[model_name])
        raw = classifier(review, truncation=True)[0]
        label = raw["label"].upper()
        score = float(raw["score"])

        if model_name == "NLP Town Product Reviews":
            stars = int(label.split()[0])
            sentiment = "Positive" if stars >= 4 else "Negative"
            st.metric("Predicted Stars", f"{stars}/5")
        elif model_name == "CardiffNLP RoBERTa":
            sentiment = "Negative" if "NEGATIVE" in label else ("Positive" if "POSITIVE" in label else "Neutral")
        else:
            sentiment = "Positive" if "POSITIVE" in label else "Negative"

        st.subheader("Result")
        st.write(f"### {sentiment}")
        st.progress(min(max(score, 0.0), 1.0))
        st.write(f"Confidence: **{score:.2%}**")
        st.caption("metadata: huggingface_AI_model")
