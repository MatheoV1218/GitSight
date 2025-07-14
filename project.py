import os
from dotenv import load_dotenv
from openai import OpenAI
from githubFetcher import fetch_github_summary
from aiAnalyzer import analyze_github_summary

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Ask for GitHub username
GitName = input("Enter a GitHub username: ")

try:
    summary = fetch_github_summary(GitName)
    ai_output = analyze_github_summary(summary, client)
    print("🔍 AI Analysis:\n")
    print(ai_output)
except ValueError as e:
    print(f"❌ Error: {e}")
