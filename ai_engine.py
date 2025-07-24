# ai_engine.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful GitHub assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error from OpenAI: {e}"
