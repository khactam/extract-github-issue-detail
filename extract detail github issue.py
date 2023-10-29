import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

TOKEN = GITHUB_TOKEN
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def get_issue_details(repo_url):
    # Convert the issue URL to the API URL for details
    api_url = repo_url.replace("github.com", "api.github.com/repos")
    
    # Fetch the issue details
    response = requests.get(api_url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    issue_data = response.json()

    # Fetch comments for the issue
    comments_url = issue_data["comments_url"]
    comments_response = requests.get(comments_url, headers=HEADERS)
    if comments_response.status_code != 200:
        print(f"Error {comments_response.status_code}: {comments_response.text}")
        return None
    comments_data = comments_response.json()

    # Extracting the issue description and comments
    details = {
        "description": issue_data["body"],
        "comments": [comment["body"] for comment in comments_data]
    }
    return details

# Read the Excel file
df = pd.read_excel("C:/Users/tamn/Downloads/extractGithubIssueProj/trialrunv1.xlsx")

# Fetch details for each GitHub issue
results = []
for _, row in df.iterrows():
    issue_id = row["Issue ID"]
    issue_title = row["Issue Title"]
    issue_link = row["Issue URL Link"]
    
    issue_data = get_issue_details(issue_link)
    results.append({
        "Issue ID": issue_id,
        "Issue Title": issue_title,
        "GitHub Link": issue_link,
        "Issue Details": str(issue_data)
    })

# Convert results to a DataFrame and save to CSV
output_df = pd.DataFrame(results)
output_df.to_csv("C:/Users/tamn/Downloads/extractGithubIssueProj/file.csv", index=False)
