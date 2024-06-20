"""
Запазва html кода на страница от форум
"""

from pickle import TRUE
import scrapy

class ForumSpider(scrapy.Spider):
    name = "_forum"
    allowed_domains = ["***"]
    start_urls = [f"https://***/forum/viewtopic.php?f=4&t={topic_id}" for topic_id in range(60000, 69000)]

    custom_settings = {
        'COOKIES_ENABLED': True,
    }

    def start_requests(self):
        cookies = {
            'phpbb3_iljl2_sid': '***',
            'phpbb3_iljl2_k':'',
            'phpbb3_iljl2_u':'1'
        }
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        print("parsing")
        page_id = response.url.split('=')[-1]
        filename = f'_forum_{page_id}.html'
        save_path = f"C:\\Users\\vikto\\Desktop\\scr\\{filename}"
        with open(save_path, 'wb') as f:
            print('saving')
            f.write(response.body)
        self.log(f'Saved file {filename}')