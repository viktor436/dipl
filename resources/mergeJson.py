"""
Събира на n на брой json файла в един 
"""

import json

def merge_json_files(file_paths, output_file_path):
    merged_data = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            merged_data.extend(data)
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(merged_data, file, ensure_ascii=False, indent=2)
    
    print(f"Merged data saved to {output_file_path}")

file_paths = [
    'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructExt.json',
    'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructAlpha.json',
    'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\forum\\forumSmall.json',
]
output_file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructULTRA.json'

merge_json_files(file_paths, output_file_path)
