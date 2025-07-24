# actions.py

from github import Github
import openai
from config import GITHUB_TOKEN, REPO_NAME, OPENAI_API_KEY, KEYWORDS

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

openai.api_key = OPENAI_API_KEY

def label_and_respond_to_issues():
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        if issue.comments == 0:  # new issue
            content = issue.title + "\n" + issue.body
            for keyword in KEYWORDS:
                if keyword.lower() in content.lower():
                    issue.add_to_labels("needs-triage")
                    print(f"Labeled issue #{issue.number}")

                    # Generate response using GPT
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are a helpful GitHub assistant."},
                            {"role": "user", "content": content}
                        ]
                    )

                    reply = response['choices'][0]['message']['content']
                    issue.create_comment(reply)
                    print(f"Replied to issue #{issue.number}")
                    break

def close_stale_issues(days=30):
    import datetime
    stale_date = datetime.datetime.now() - datetime.timedelta(days=days)
    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        if issue.updated_at < stale_date:
            issue.create_comment("This issue has been automatically closed due to inactivity.")
            issue.edit(state='closed')
            print(f"Closed stale issue #{issue.number}")
