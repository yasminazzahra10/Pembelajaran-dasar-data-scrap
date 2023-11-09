import os
from bs4 import BeautifulSoup
import requests
import fungsi

def main_scraper(url,directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text,"html.parser")
    articles = soup.find_all("h3",{'class':'article__title article__title--medium'})
    for article in articles:
        print(article.a.get("href"))
        print(article.text)

main_scraper("https://www.kompas.com/","Hasil")
