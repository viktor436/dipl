"""
Прави диаграма на разпределението на дължините на въпросите и отговорите от json файл
"""

import json
import pandas as pd
import matplotlib.pyplot as plt

def plot_qa_lengths(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    
    df['Question Length'] = df['Question'].apply(len)
    df['Answer Length'] = df['Answer'].apply(len)
    
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    ax[0].hist(df['Question Length'], bins=20, color='skyblue', edgecolor='black')
    ax[0].set_title('Distribution of Question Text Lengths')
    ax[0].set_xlabel('Length')
    ax[0].set_ylabel('Frequency')
    
    ax[1].hist(df['Answer Length'], bins=20, color='salmon', edgecolor='black')
    ax[1].set_title('Distribution of Answer Text Lengths')
    ax[1].set_xlabel('Length')
    ax[1].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

json_file_path = 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\instruct\\uncleaned\\formated\\bglawinstructULTRA.json'  # Replace with your file path
plot_qa_lengths(json_file_path)
