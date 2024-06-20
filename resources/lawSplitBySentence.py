"""
Зарежда файл със един нормативен акт и го разделя на изречения като за всяко изречение включва от кой норматвен акт е
"""
import json
import re

def split_text(text):
    pattern = r'(?<=\.)\s+(?=\(\d+\)\s+[A-ZА-Я][a-zа-я])|(?<=\.)\s+(?=[A-ZА-Я][a-zа-я])'
    sentences = re.split(pattern, text)
    return sentences

def split_json_by_sentences(json_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as input_file, \
         open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            try:
                entry = json.loads(line) 
                sentences = split_text(entry['SENTENCE'])
                for sentence in sentences:
                    new_entry = {
                        "LAW": entry['LAW'],
                        "SENTENCE": sentence.strip()
                    }
                    json.dump(new_entry, output_file, ensure_ascii=False)
                    output_file.write('\n')
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
            except KeyError as e:
                print(f"Missing key in JSON object: {e}")

split_json_by_sentences('C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\output6.json', 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\json\\output5.json')
