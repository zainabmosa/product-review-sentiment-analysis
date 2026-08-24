# 🛍️ Product Review Sentiment Analysis

## About the Project

In this project, I used pretrained models from Hugging Face to analyze product reviews.

The main idea of the project is to see if a review is **Positive** or **Negative** without training a model from scratch.

I also compared different pretrained models to see which one performed better on my dataset.

---

## 🎯 Problem

Many businesses receive a large number of customer reviews, so reading every review manually can take a lot of time.

In this project, I used pretrained sentiment analysis models to automatically analyze product reviews.

The input is a product review, and the model predicts whether the sentiment is positive or negative.

---

## 📊 Dataset

I used a dataset called:

`product_reviews.csv`

The dataset contains **100 product reviews**:

* 50 Positive reviews
* 50 Negative reviews

I used this dataset to test and evaluate the pretrained models.

---

## 🤖 Models Used

I tested three pretrained models from Hugging Face:

### DistilBERT-SST2

`distilbert/distilbert-base-uncased-finetuned-sst-2-english`

### NLP Town BERT

`nlptown/bert-base-multilingual-uncased-sentiment`

### CardiffNLP RoBERTa

`cardiffnlp/twitter-roberta-base-sentiment-latest`

---

## 🔍 What I Did

In the notebook, I:

* Defined the problem
* Prepared the dataset
* Selected pretrained models
* Checked information about the models
* Ran predictions on the reviews
* Evaluated the models
* Used different evaluation metrics
* Created confusion matrices
* Checked incorrect predictions
* Compared the models
* Looked at possible domain differences
* Tried Zero-Shot Classification
* Selected the best model based on the results

---

## 📈 Evaluation

I used the following metrics to evaluate the models:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Inference Time

---

## 🧪 Zero-Shot Classification

I also tried Zero-Shot Classification using a pretrained Hugging Face model.

I classified product reviews into different topics:

* Product Quality
* Price and Value
* Delivery
* Usability and Performance
* Description Match

The Zero-Shot model I used was:

`facebook/bart-large-mnli`

---

## 🖥️ Streamlit Application

I created a simple Streamlit application called **Review Mood Checker**.

The user can:

1. Write a product review
2. Click **Analyze Review**
3. See if the review is Positive or Negative
4. See the confidence score

### 🚀 Try the App

[Open Review Mood Checker](https://appuct-review-sentiment-analysis.streamlit.app/?utm_source=chatgpt.com)

---

## 📁 Project Files

```text
product-review-sentiment/
│
├── product_review_sentiment_complete.ipynb
├── product_reviews.csv
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

To run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🛠️ Tools and Libraries

For this project, I used:

* Python
* Pandas
* Hugging Face Transformers
* PyTorch
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## 👩‍💻 Author

**Zainab Mohammed**
**Data Science**
