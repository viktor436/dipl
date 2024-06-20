"""
Създава база от данни с въпроси и отговори с помоща на модел на OpenAI
"""
from openai import OpenAI
import json
import os
import time

def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            raise ValueError("Invalid JSON format. Expected a list of dictionaries.")

def save_response(response):
    with open("C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\openai\\QAoutput3.json", "a", encoding='utf-8') as f:
        if isinstance(response, bytes):
            response = response.decode('utf-8')
        serializable_response = {"text": str(response)}
        json.dump(serializable_response, f, ensure_ascii=False)
        f.write("\n")

def make_api_call(client, pair):
    try:
        completion = client.chat.completions.create(
            temperature=0.9,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a law assistant. You should generate question/answer pairs on given text, you don't have prior knowledge."},
                {"role": "user", "content": f"Генерирай двойки въпрос и отговор върху този правен текст от {pair.get('law', '')} на България: {pair.get('text', '')}"}
            ]
        )
        return completion
    except Exception as e:
        print(f"Error: {e}")
        raise

def main():
    if "OPENAI_API_KEY" not in os.environ:
        raise ValueError("API key not found")
    
    client = OpenAI()

    law_sentence_pairs = load_prompt("C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\openai\\LAW_ARTICLE_SPLIT_LAWS2.json")
    delay = 60

    for pair in law_sentence_pairs:
        retry = 0
        while retry < 30:
            try:
                completion = make_api_call(client, pair)
                print("Response from OpenAI:")
                print(completion.choices[0].message)
                print()
                response_content = completion.choices[0].message
                response = {"text": response_content}
                save_response(response)
                break
            except Exception as e:
                print(f"Attempt {retry + 1} failed; retrying with next entry after {delay} seconds.")
                time.sleep(delay)
                retry += 1
                if retry >= 2:
                    print("Max retries reached for this pair. Moving to the next pair.")
                    break

    print("Responses saved to responses.json")

if __name__ == "__main__":
    main()
