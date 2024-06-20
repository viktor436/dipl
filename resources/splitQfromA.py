"""
 Превръща един ред от json файла от тип текст съдържащ "Въпрос:" и "Отговор:" в ред с две промеливи а именно Question и Answer
 Така например     {"text": "Въпрос: Кога влиза в сила Валутният закон на България?\\nОтговор: В сила влиза от 01.01.2000 г."} става  
{
    "Question": "Кога влиза в сила Валутният закон на България?",
    "Answer": "В сила влиза от 01.01.2000 г."
  },"""

import json
import re

def parse_qa(text):
    parts = re.split("Въпрос:|Отговор:", text)
    parts = [part.strip() for part in parts if part.strip()]
    
    qa_pairs = []
    for i in range(0, len(parts), 2):
        qa_pairs.append({"Question": parts[i], "Answer": parts[i+1] if i+1 < len(parts) else ""})
    return qa_pairs

def convert_json_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    new_data = []
    for entry in data:
        text = entry["text"]
        qa_pairs = parse_qa(text)
        new_data.extend(qa_pairs)
    
    return new_data

input_file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\QAoutput2.json'  # input path
output_file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructAlpha.json'  # save path

converted_data = convert_json_format(input_file_path)

with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(converted_data, file, ensure_ascii=False, indent=2)

print(f"Converted data saved to {output_file_path}")
