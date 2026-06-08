from flask import Flask, render_template, request
import os
from bot import get_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]

    answer = get_answer(question)


    return render_template(
    "index.html",
    answer=answer,
    question=question
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",500))
    app.run( host="0.0.0.0",port =port)
