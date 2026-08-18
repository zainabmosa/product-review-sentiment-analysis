# 🛍️ Product Review Sentiment Analysis

## 1. Problem Definition
This project analyzes product reviews and classifies them as positive or negative using pretrained models from the Hugging Face Model Hub.

## 2. Data Collection
A small evaluation dataset of 100 manually-created product reviews was prepared for this lab: 50 positive and 50 negative examples.

## 3. Data Preparation
The dataset contains two columns:
- `review`
- `label`

## 4. Model Selection
Three pretrained Hugging Face models are compared:
1. `distilbert/distilbert-base-uncased-finetuned-sst-2-english`
2. `nlptown/bert-base-multilingual-uncased-sentiment`
3. `cardiffnlp/twitter-roberta-base-sentiment-latest`

## 5. Model Card Investigation
Model-card information is documented in the notebook. Official cards:
- https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english
- https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment
- https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest

## 6. Initial Inference Results
The notebook runs every model on all 100 reviews and stores the label, confidence score, raw label, and the required metadata field.

## 7. Evaluation
Accuracy, Precision, Recall, F1-score, confusion matrices, and inference time are calculated.

## 8. Error Analysis
Misclassified reviews are extracted automatically. At least 10 interesting failures should be discussed in the final report when applicable.

## 9. Model Comparison
The models are compared using performance, inference speed, model size, language support, training domain, and failure cases.

## 10. Limitations
- The evaluation dataset is small.
- The reviews are manually created rather than collected from a large real-world source.
- The evaluation is English-only.
- Some models were trained on domains different from product reviews.
- The NLP Town model predicts 1–5 stars and is converted to binary sentiment for this experiment.
- CardiffNLP has a neutral class; the notebook maps neutral to positive for the binary comparison, which is a limitation.

## 11. Final Recommendation
Run the notebook first and replace this section with the actual best model and evidence from the results.

## 12. Future Work / Fine-Tuning Proposal
A larger real-world product-review dataset could be collected. If performance remains weak, a sentiment model could be fine-tuned on domain-specific product reviews and compared with the original pretrained models.

## How to Run

### Notebook
Open `product_review_sentiment.ipynb` in Google Colab or Jupyter. Upload `product_reviews.csv` to the same working directory, then run the cells from top to bottom.

### Streamlit
```bash
pip install -r requirements.txt
streamlit run app.py
```
