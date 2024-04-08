import requests
import json

# GitHub API endpoint for creating a repository
url = "https://api.github.com/orgs/{organization}/repos"

# Personal access token (Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your token)
token = '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'

# Organization name
organization = 'IBM-batch'

# Repository name
repo_name = 'new_repo'

# Request headers
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# Request payload
payload = {
    "name": repo_name,
    "private": False  # Set to True if you want to create a private repository
}

# Make POST request to create repository
response = requests.post(url.format(organization=organization), headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 201:
    print(f"Repository '{repo_name}' created successfully in the organization '{organization}'.")
else:
    print(f"Failed to create repository. Status code: {response.status_code}, Error message: {response.text}")

