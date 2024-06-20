"""
Премахва излишно колиество точки в текст. Пример: "Име: ............................................ Фамилия: ............................................ става Име: .... Фамилия: ....
"""

import json
import re

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def replace_excessive_fullstops(data):
    pattern = r'\.{6,}'
    for entry in data:
        entry['text'] = re.sub(pattern, '...', entry['text'])
    return data

def write_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

input_json_filename = 'output_document.json'  # вход
output_json_filename = 'modified_output_document.json'

json_data = read_json(input_json_filename)

modified_data = replace_excessive_fullstops(json_data)

write_json(modified_data, output_json_filename)
