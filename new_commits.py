import json
from datetime import datetime, timedelta, timezone
import requests

# Replace with your GitHub username and repository
GITHUB_USERNAME = "debrej2021"
REPOSITORY_NAME = "Build_CI_CD"
ACCESS_TOKEN = "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"  # Optional: Use a personal access token if needed

# GitHub API URL for commits
COMMITS_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPOSITORY_NAME}/commits"

# Optional: Set a date range to check for commits (e.g., commits from the last 24 hours)
since_date = datetime.now(timezone.utc) - timedelta(days=1)
since_date_str = since_date.strftime('%Y-%m-%dT%H:%M:%SZ')

# Headers for authentication (optional)
headers = {
    "Authorization": f"token {ACCESS_TOKEN}"
} if ACCESS_TOKEN else {}

# Parameters to filter commits
params = {
    "since": since_date_str
}

# Fetch commits from the GitHub API
response = requests.get(COMMITS_URL, headers=headers, params=params)

if response.status_code == 200:
    commits = response.json()
    if commits:
        print(f"Found {len(commits)} new commit(s) since {since_date_str}:\n")
        for commit in commits:
            commit_message = commit['commit']['message']
            commit_author = commit['commit']['author']['name']
            commit_date = commit['commit']['author']['date']
            commit_url = commit['html_url']
            print(f"Commit by {commit_author} on {commit_date}")
            print(f"Message: {commit_message}")
            print(f"URL: {commit_url}\n")
    else:
        print(f"No new commits found since {since_date_str}.")
else:
    print(f"Failed to fetch commits. Status code: {response.status_code}")
    print(f"Response: {response.text}")
