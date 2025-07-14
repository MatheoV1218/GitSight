# GitSight 🔍

GitSight is a Python-based tool that analyzes any public GitHub user's profile and provides a **smart summary** of their repositories — including stars, programming languages, and more. It's designed to be beginner-friendly, recruiter-useful, and a great way for developers to review or showcase their GitHub activity.

---

## 🚀 Features

- 🔎 **Enter any GitHub username**
- 📦 Lists all **public repositories**
- ⭐ Counts **total stars** received across all repos
- 🧠 Identifies the **most used programming language**
- 📋 Shows each repo's:
  - Name
  - Primary language
  - Description
  - Star count
  - Last updated time
  - Languages used (via GitHub's language API)
- ❌ Handles common errors:
  - Invalid usernames
  - Users with no public repositories
  - Rate limits or API issues

---

## 👤 Who Is This For?

- **Job Seekers:** Use it to scan your own profile and identify resume-worthy highlights
- **Recruiters:** Quickly assess a candidate’s GitHub activity and repo quality
- **Educators/Peers:** Review student or peer coding portfolios
- **Hackers & Builders:** Use it as a base to build something bigger (AI suggestions, visual dashboards, web app)

---

## 🖥️ Demo Output Example


---

## ⚙️ How It Works

1. The user inputs a **GitHub username**
2. GitSight calls the **GitHub REST API** to fetch:
   - Profile info
   - Public repositories
   - Language data for each repo
3. It summarizes the data and prints it to the terminal

---

## 🛠️ Technologies Used

- **Python 3.x**
- `requests` (for API calls)
- GitHub REST API v3

---

## 📦 Installation & Usage

### ✅ Requirements
- Python 3.x installed
- Internet connection

### 🧪 Run It Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/MatheoV1218/GitSight.git
   cd GitSight
