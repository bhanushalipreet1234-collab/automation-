from github import Github
from config import GITHUB_TOKEN, REPO_NAME, KEYWORDS

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

def label_and_respond_to_issues():
    issues = repo.get_issues(state="open")
    for issue in issues:
        for keyword in KEYWORDS:
            if keyword.lower() in issue.title.lower():
                issue.add_to_labels(keyword)
                issue.create_comment(f"🔍 AI detected this as a `{keyword}` issue.")
                break

def close_stale_issues(days_stale=30):
    from datetime import datetime, timedelta
    issues = repo.get_issues(state="open")
    cutoff = datetime.utcnow() - timedelta(days=days_stale)

    for issue in issues:
        if issue.updated_at < cutoff:
            issue.create_comment("⏳ This issue has been automatically closed due to inactivity.")
            issue.edit(state="closed")
