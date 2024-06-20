"""
Разделя на случаен принцип jsonl файл на две като прилага 80/20 процента разпределение на данните между файловете
"""

import json

source_jsonl_file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\jsonl\\combined.jsonl'

output_jsonl_file_80_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\jsonl\\output_file_80.jsonl'
output_jsonl_file_20_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\jsonl\\output_file_20.jsonl'

with open(source_jsonl_file_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

split_index = int(len(data) * 0.8)

data_80 = data[:split_index]
data_20 = data[split_index:]

with open(output_jsonl_file_80_path, 'w', encoding='utf-8') as file:
    for item in data_80:
        file.write(json.dumps(item, ensure_ascii=False) + '\n')

with open(output_jsonl_file_20_path, 'w', encoding='utf-8') as file:
    for item in data_20:
        file.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f'Successfully split the file into 80% and 20% portions at:\n{output_jsonl_file_80_path}\n{output_jsonl_file_20_path}')
