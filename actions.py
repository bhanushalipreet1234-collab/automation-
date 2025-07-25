from github import Github
import os

TOKEN = os.getenv("GITHUB_TOKEN") or "your_token_here"
REPO_NAME = "your_username/your_repo"

g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)

def label_and_respond_to_issues():
    issues = repo.get_issues(state='open')
    for issue in issues:
        if not issue.labels:
            issue.create_comment("Thanks for opening this! We'll triage it shortly.")
            issue.add_to_labels("triage")

def close_stale_issues():
    issues = repo.get_issues(state='open')
    for issue in issues:
        if "stale" in [label.name for label in issue.labels]:
            issue.create_comment("Closing due to inactivity.")
            issue.edit(state="closed")
