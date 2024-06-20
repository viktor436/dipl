"""
Проверява дали json ред съдържа повече от едн двойка "Въпрос:" and "Отговор:" (възможен дефект при синтетично генерираната база данни). Aко се съдържа принтира проблемния ред
"""
import json
import re

def has_complete_pairs(line):
    pair_pattern = re.compile(r'Въпрос:.*?Отговор:')
    pairs = pair_pattern.findall(line)
    questions_count = line.count("Въпрос:")
    answers_count = line.count("Отговор:")
    return questions_count == answers_count and questions_count == len(pairs)

with open('C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\QAoutput2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

line_number = 1

for entry in data:
    text = entry.get("text", "")
    lines = text.split('\n')
    for line in lines:
        if not has_complete_pairs(line):
            print(f"Problematic line number: {line_number}")
        line_number += 1
