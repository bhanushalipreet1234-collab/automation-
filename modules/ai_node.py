import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def handle_ai_node(input_text, model="gpt-4"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an automation assistant."},
                {"role": "user", "content": input_text}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"OpenAI Error: {e}"
