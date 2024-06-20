"""
Събира n на брой текстови файла в един
"""
filenames = ["C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts0_prep.txt", 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts1_prep.txt', 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts2_prep.txt', 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts3_prep.txt', 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts4_prep.txt', 'C:\\Users\\vikto\\Desktop\\vikuniaq\\diplomworkAll\\resources\\datasets\\prepared\\txt\\extracted_cleaned_texts5_prep.txt']

with open('cleaned_texts_prep_all.txt', 'w', encoding="utf-8") as outfile:
    for fname in filenames:
        with open(fname, encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content)
            # separation between texts from different files
            outfile.write('\n')

print('Files have been successfully merged into merged.txt')
