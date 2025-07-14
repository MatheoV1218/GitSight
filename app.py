from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from githubFetcher import fetch_github_summary
from aiAnalyzer import analyze_github_summary
from openai import OpenAI

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("github_username")
        try:
            summary = fetch_github_summary(username)
            analysis_data = analyze_github_summary(summary, client)

            return render_template("index.html",
                                   username=username,
                                   strengths=analysis_data["strengths"],
                                   weaknesses=analysis_data["weaknesses"],
                                   suggestions=analysis_data["suggestions"],
                                   projects=analysis_data["projects"])
        except ValueError as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
