# 📧 Predictive Email/Spam Detection using Machine Learning

This repository, titled **MACHINE-LEARNING-MODEL-IMPLEMENTATION**, contains a complete end-to-end machine learning project developed as part of a 6-week internship at **CodTech IT Solutions**. The project focuses on building and deploying an intelligent system for detecting **spam emails or messages** using **Natural Language Processing (NLP)** and **Streamlit**.

The model processes raw text messages, extracts features, classifies the content as **spam** or **ham**, and provides a simple web interface for live testing.

---


## 🚀 Key Features

✅ End-to-end spam detection pipeline  
✅ Text preprocessing using NLP (NLTK)  
✅ TF-IDF vectorization of message content  
✅ Classification using Multinomial Naive Bayes  
✅ Deployment using Streamlit for real-time testing  
✅ Modular and readable codebase with `.py` and `.ipynb` files  
✅ Reproducible training pipeline with dataset and requirements file  

---

## 🧠 Technologies Used

| Tool/Library | Purpose |
|--------------|---------|
| **Python 3** | Programming language |
| **Pandas** | Data manipulation |
| **NLTK** | Natural Language Processing |
| **Scikit-learn** | ML model & metrics |
| **Streamlit** | Web deployment |
| **Jupyter Notebook** | Exploratory development |
| **GitHub** | Version control & collaboration |

---

## 📁 Folder Structure

```
MACHINE-LEARNING-MODEL-IMPLEMENTATION/
│
├── app.py                      # Streamlit web app for live predictions
├── model.pkl                   # Trained Naive Bayes model
├── vectorizer.pkl              # TF-IDF vectorizer
├── spam.csv                    # Dataset (SMS Spam Collection)
├── sms-spam-classifier.ipynb   # Jupyter notebook (EDA + training)
├── requirements.txt            # Required Python libraries
├── setup.sh                    # Shell script for environment setup (for deployment)
├── nltk.txt                    # NLTK corpora required
├── Procfile                    # For Streamlit/Heroku deployment
└── README.md                   # You're here!
```

---

## 📊 Dataset

We use the [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection), a well-known dataset consisting of over 5,500 SMS messages labeled as “spam” or “ham”.

Each message is passed through a preprocessing pipeline and then converted into numerical features using TF-IDF vectorization.

---

## ⚙️ How to Run

### 🛠️ Installation

```bash
git clone https://github.com/your-username/MACHINE-LEARNING-MODEL-IMPLEMENTATION.git
cd MACHINE-LEARNING-MODEL-IMPLEMENTATION
pip install -r requirements.txt
```

### 📦 Download NLTK Corpora

Run this once to download required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

### ▶️ Run Streamlit App

```bash
streamlit run app.py
```

Open the link in your browser and test the spam detection live with sample inputs!

---

## 🧪 Sample Test

**Input:**  
> "Congratulations! You've been selected for a free iPhone. Click here to claim."

**Prediction:**  
> `Spam ✅`

**Input:**  
> "Hey, I’ll see you at the meeting at 3 PM. Don’t be late!"

**Prediction:**  
> `Ham ✅`

---

## 📈 Model Performance

- **Accuracy:** ~98%
- **Precision:** 99%
- **Recall:** 96.5%
- **F1-Score:** 97.1%

The model demonstrates excellent performance on the test dataset, with minimal false positives/negatives.

---

## 🌐 Deployment

The model is deployed using **Streamlit**, which offers a fast and interactive UI to test inputs in real time. This makes it useful for:

- Live demonstrations  
- Classroom presentations  
- Client showcases  
- Prototyping future APIs

---

## 👨‍💻 Author

**Tushar Singh**  
Third-Year ECE, NIT Kurukshetra  
ML & AI | Python | NLP | Open Source  
📧 [tusharsinghthakur1212@gmail.com]  
🔗 [www.linkedin.com/in/tushar-singh-9a22582bb]

---

## 📝 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share it with proper attribution.

---

## 🙌 Acknowledgements

- CodTech IT Solutions for mentorship and opportunity  
- UCI ML Repository for the dataset  
- Open-source libraries that made this possible  
