"""
Изпраща заявки до api-то на OpenAI
"""
from openai import OpenAI
import os

def make_api_call(client, text):
    try:
        completion = client.chat.completions.create(
            temperature=0.9,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a chatbot."},
                {"role": "user", "content": text}
            ]
        )
        return completion
    except Exception as e:
        print(f"Error: {e}")
        raise

def main():
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("API key not found!!!")
    
    client = OpenAI()

    text = "What is the weather like today?"
    
    try:
        completion = make_api_call(client, text)
        print("Response from OpenAI:")
        print(completion.choices[0].message)
    except Exception as e:
        print("Failed to obtain response:", e)

if __name__ == "__main__":
    main()
