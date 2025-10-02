# 🌍 Multilingual Sentiment Analyzer

A **beautiful Flask web app** that detects sentiment (`Positive`, `Neutral`, `Negative`) in **any language** using **XLM-RoBERTa**, a state-of-the-art multilingual NLP model. Perfect for demos, prototypes, or experimenting with multilingual text analytics.  

---

## 🖥️ Features
- Detect sentiment in **100+ languages** including English, Hindi, Spanish, French, German, and more.  
- Displays **sentiment emojis** (😊 😐 😡) for instant visualization.  
- Shows **confidence scores** with a dynamic color-coded bar.  
- Sleek, modern, and responsive web interface built with **Flask + HTML/CSS**.  
- Lightweight, easy to deploy locally or on cloud platforms.  

---

## 🚀 Demo Screenshots

| Input (English) | Input (Hindi) | Input (Spanish) |
|-----------------|---------------|----------------|
| 😊 Positive     | 😊 Positive    | 😡 Negative    |

*(Add actual screenshots here after running the app for demo)*

---

## 💻 Installation

1. **Clone the repository**  

```bash
git clone <repo-url>
cd multilingual-sentiment-analyzer
```

2. **Install dependencies**
```bash
pip install flask transformers torch
```

3. **Run Locally**

```bash
python app.py
```

Open your browser and go to:

```bash
http://127.0.0.1:5000
```

Type any text in any language and click Analyze Sentiment.
<img width="732" height="822" alt="image" src="https://github.com/user-attachments/assets/d2c43174-6b77-400c-89f6-cdac5e7e7605" />
<img width="716" height="801" alt="image" src="https://github.com/user-attachments/assets/3bafcaf8-5f3d-4850-a706-dcc3d5a3d5fe" />
<img width="679" height="813" alt="image" src="https://github.com/user-attachments/assets/38cc329e-fd8f-492d-9cb6-d4ea009fbf54" />

