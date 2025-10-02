from flask import Flask, render_template, request
from transformers import pipeline

# Load multilingual sentiment model once
classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-xlm-roberta-base-sentiment"
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():
            result = classifier(text)[0]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
