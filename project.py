import requests
import sys

# Step 1: Validate username
while True:
    GitName = input("Enter a GitHub username: ")
    profile_url = f"https://api.github.com/users/{GitName}"
    profile_response = requests.get(profile_url)

    if profile_response.status_code == 200:
        break
    elif profile_response.status_code == 403:
        print("API limit reached or profile is blocked.")
    else:
        print("Not a valid username.")

# Step 2: Fetch their repositories
repo_url = f"https://api.github.com/users/{GitName}/repos"
response = requests.get(repo_url)
data = response.json()
if not data:
    print("There are no repositories on this profile")
    sys.exit()

# All the variables to be used in the for loop
RepoCount = 0
languageCount = {}
StarCount = 0
MostStars = 0

print("Github profile summary for: " + GitName)
# Go through each repo
for repo in data:
    print("----------------------------")
    print(f"Repo Name: {repo['name']}")
    RepoCount += 1
    if repo['language'] is None:
        print("Language: Not specified")
    else:
        print(f"Primary Language: {repo['language']}")
    print(f"Stars: {repo['stargazers_count']}")
    StarCount += repo['stargazers_count']
    if repo['description'] is None:
        print("No description")
    else:
        print(f"Description: {repo['description']}")
    print(f"URL: {repo['html_url']}")
    print(f"Last Updated: {repo['updated_at']}")

    # NEW: Fetch all languages used in this repo
    lang_url = f"https://api.github.com/repos/{GitName}/{repo['name']}/languages"
    lang_response = requests.get(lang_url)
    lang_data = lang_response.json()

    if lang_data:
        language_list = ", ".join(lang_data.keys())
        print(f"Languages used: {language_list}")
    else:
        print("Languages used: Not available")

    for language in lang_data.keys():
        if language in languageCount:
            languageCount[language] += 1
        else:
            languageCount[language] = 1
        
mostUsedLanguage = max(languageCount, key = languageCount.get)
print("Total Repositories: " + str(RepoCount))
print("Total stars: " + str(StarCount))
print("Most used language: " + mostUsedLanguage)

