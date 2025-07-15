# 🔍 GitSight

**GitSight** is an AI-powered web app that analyzes any public GitHub profile and summarizes it into strengths, weaknesses, suggestions for improvement, and personalized project recommendations.

It’s perfect for developers who want quick feedback on their GitHub presence without reading through every repo manually.

---

## 💡 Features

- 🔍 Analyze any public GitHub username
- 📊 Clear feedback on coding strengths and weaknesses
- 🧠 AI-generated suggestions for improvement
- 🧪 Project ideas tailored to your skillset
- 📦 Clean, responsive UI with categorized results

---

## 🧠 How It Works

1. The user enters a GitHub username.
2. The app uses the GitHub REST API to fetch all public repositories.
3. It compiles relevant information like:
   - Repo name
   - Description
   - Star count
   - Primary language
   - Last updated time
   - README presence
   - Total commits (approximate)
4. This summary is sent to OpenAI’s API for analysis.
5. The response is parsed and displayed in four sections:
   - Strengths
   - Weaknesses
   - Suggestions
   - What to Build Next

---

## 🛠️ Tech Stack

| Category   | Tools/Frameworks             |
|------------|------------------------------|
| Backend    | Python, Flask                |
| Frontend   | HTML, CSS                    |
| APIs       | GitHub REST API, OpenAI API  |
| Security   | dotenv (.env) for API keys   |

---

## 🧪 Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/MatheoV1218/GitSight.git
cd GitSight
