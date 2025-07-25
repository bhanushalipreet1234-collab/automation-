import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def handle_ai_node():
    prompt = "Summarize recent GitHub issues and suggest labels."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print("AI Response:", response["choices"][0]["message"]["content"])
