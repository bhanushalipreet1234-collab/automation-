from github import Github
from config import GITHUB_TOKEN, REPO_NAME

def handle_github_issue(title, body):
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        issue = repo.create_issue(title=title, body=body)
        return f"Issue created: #{issue.number}"
    except Exception as e:
        return f"GitHub Error: {e}"
