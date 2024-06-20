"""
Избира на случаен принцип обекти(редове) от json файла и ги запазва в нов
"""

import json
import random

def reduce_json_file(input_file, output_file, target_count=10000):
    # Load JSON data from file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Check if the file has more than target_count objects
    total_objects = len(data)
    if total_objects <= target_count:
        print("The original file has less or equal objects than the target count.")
        return

    # Randomly select objects until only target_count objects are left
    reduced_data = random.sample(data, target_count)

    # Write the reduced data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(reduced_data, file, ensure_ascii=False, indent=2)
    
    print(f"Reduced file written with {target_count} objects.")

# Example usage
input_filename = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructAlpha.json'
output_filename = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructAlphaMINI.json'
reduce_json_file(input_filename, output_filename)
