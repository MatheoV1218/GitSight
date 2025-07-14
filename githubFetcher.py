import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Get the GitHub token from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Set the headers for authenticated requests
headers = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_github_summary(GitName: str) -> str:
    # Step 1: Validate GitHub username
    profile_url = f"https://api.github.com/users/{GitName}"
    profile_response = requests.get(profile_url, headers=headers)
    if profile_response.status_code == 403:
        raise ValueError("API limit reached or profile is blocked.")
    elif profile_response.status_code != 200:
        raise ValueError("Not a valid username.")

    # Step 2: Fetch repositories
    repo_url = f"https://api.github.com/users/{GitName}/repos"
    response = requests.get(repo_url, headers=headers)
    data = response.json()
    if not data:
        raise ValueError("There are no repositories on this profile")

    # Collect data
    RepoCount = 0
    languageCount = {}
    StarCount = 0
    totalCommits = 0
    summary = f"GitHub summary for user: {GitName}\n\n"

    for repo in data:
        summary += "----------------------------\n"
        summary += f"Repo Name: {repo['name']}\n"
        RepoCount += 1

        language = repo['language'] if repo['language'] else "Not specified"
        summary += f"Primary Language: {language}\n"
        StarCount += repo['stargazers_count']
        summary += f"Stars: {repo['stargazers_count']}\n"

        description = repo['description'] if repo['description'] else "No description"
        summary += f"Description: {description}\n"
        summary += f"URL: {repo['html_url']}\n"
        summary += f"Last Updated: {repo['updated_at']}\n"

        # Check README
        readme_url = f"https://api.github.com/repos/{GitName}/{repo['name']}/readme"
        readme_response = requests.get(readme_url, headers=headers)
        has_readme = "✅" if readme_response.status_code == 200 else "❌"
        summary += f"README: {has_readme}\n"

        # Languages
        lang_url = f"https://api.github.com/repos/{GitName}/{repo['name']}/languages"
        lang_response = requests.get(lang_url, headers=headers)
        lang_data = lang_response.json()

        if lang_data:
            language_list = ", ".join(lang_data.keys())
            summary += f"Languages used: {language_list}\n"
        else:
            summary += "Languages used: Not available\n"

        for lang in lang_data:
            languageCount[lang] = languageCount.get(lang, 0) + 1

       

        summary += "\n"

    mostUsedLanguage = max(languageCount, key=languageCount.get)
    summary += "----------------------------\n"
    summary += f"Total Repositories: {RepoCount}\n"
    summary += f"Total Stars: {StarCount}\n"
    summary += f"Most Used Language: {mostUsedLanguage}\n"

    return summary
