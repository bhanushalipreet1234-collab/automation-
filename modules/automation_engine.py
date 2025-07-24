from modules.ai_node import handle_ai_node
from modules.github_node import handle_github_issue

def execute_flow(data):
    if not data or "drawflow" not in data or "Home" not in data["drawflow"]:
        print("Invalid flow data")
        return

    nodes = data["drawflow"]["Home"]["data"]
    for node_id, node in nodes.items():
        if node["name"] == "OpenAI":
            prompt = node["data"].get("prompt", "Hello!")
            output = handle_ai_node(prompt)
            print(f"[OpenAI] → {output}")
        elif node["name"] == "GitHub":
            title = node["data"].get("title", "New Issue")
            body = node["data"].get("body", "Created via automation")
            print(handle_github_issue(title, body))
