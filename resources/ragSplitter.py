"""
Разделя текстов файл със нормативни актове по членове като добавя наредбата от която е члена пред всеки член.
Пример: <$>Валутен закон<S>Чл. 1 Златото и среброто са скъпоценни метали</$>
"""
import re
import pandas as pd

def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def split_document(text):
    law_pattern = r"\$([A-ZА-Я0-9][A-ZА-Я0-9\s,-]+)\s(?=[A-ZА-Я])"
    article_pattern = r'(?=Чл\. \d+[\wа-яА-Я]*)'

    law_matches = [(match.group(1), match.start(), match.end()) for match in re.finditer(law_pattern, text, re.DOTALL)]
    result = []

    for i, (law, start, end) in enumerate(law_matches):
        law_text = text[end:law_matches[i + 1][1]] if i < len(law_matches) - 1 else text[end:]
        
        articles = re.split(article_pattern, law_text)
        for article in articles:
            if article.strip():
                formatted_part = f"<$>{law}<S>{article.strip()}</$>"
                result.append(formatted_part)

    return result

def write_to_file(output_text, filename):
    content = '\n'.join(output_text)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

input_filename = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\cleaned_texts_prep_all.txt'
output_filename = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\helpers\\RAG\\output_RAG_SPLIT_WITH_LAW.txt'

input_text = read_from_file(input_filename)

splits = split_document(input_text)

write_to_file(splits, output_filename)
