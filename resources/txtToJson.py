"""
Зарежда нормативен акт от текстов файл и го запазва във json файл като запазва името на нормативния акт. Резултатът е разделени по ннормативни актове текстове.
"""
from ast import pattern
import pandas as pd
import re

file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts5_prep.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Regex pattern to find 'LAW' parts
pattern = r"\$([A-ZА-Я0-9][A-ZА-Я0-9\s,-]+)\s(?=[A-ZА-Я])"

matches = [(match.group(), match.start(), match.end()) for match in re.finditer(pattern, text, re.DOTALL)]

data = []

for i, (law, start, end) in enumerate(matches):
    if i < len(matches) - 1:
        sentence = text[end:matches[i + 1][1]].strip()
    else:
        sentence = text[end:].strip()
    
    data.append([law, sentence])

df = pd.DataFrame(data, columns=['LAW', 'SENTENCE'])


json_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\output5.json'
df.to_json(json_path, orient='records', force_ascii=False, lines=True)