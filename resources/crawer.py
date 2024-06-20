import requests
from bs4 import BeautifulSoup

def fetch_and_parse_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Successfully fetched: {url}")
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to fetch {url}")
        return None
    
def extract_specific_links(soup, base_url):
    links = soup.find_all('a', class_='law', href=True)
    specific_links = [link['href'] for link in links]
    if not specific_links:
        print("No specific links found on the page.")
    return specific_links

def crawl_and_extract_text_to_file(start_url, end_url, base_url, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(start_url, end_url + 1):
            page_url = f"{base_url}/bg/laws/tree/ords/{i}"
            print(f"\nProcessing page: {page_url}")
            soup = fetch_and_parse_url(page_url)
            if soup:
                specific_links = extract_specific_links(soup, base_url)
                for link in specific_links:
                    sub_soup = fetch_and_parse_url(link)
                    if sub_soup:
                        text = sub_soup.get_text(separator=' ', strip=True)
                        if text:
                            file.write(text + '\n\n' + '$')
                            print(f"Saved text from {link} to file.")
                        else:
                            print(f"No text extracted from {link}")

# Config
base_url = "https://***"
file_name = "data.txt"

crawl_and_extract_text_to_file(0, 70, base_url, file_name)