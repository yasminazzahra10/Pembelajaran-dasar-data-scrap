import os
from bs4 import BeautifulSoup
import requests
import fungsi

def get_detail(url, directory):
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    articles = soup.find_all("article", {'class' : 'article-post'})

    for article in articles :
        print("Judul :" + article.find("h2").text)
        isi = article.find_all("p")
        for p in isi:
            print(p.text)
        print()

        article_format = "Judul : " + article.find("h2").text + "\n\n"
        for p in isi:
            article_format += p.text + "\n"

        if fungsi.does_file_exist(directory + "artikel.doc") is False:
            fungsi.create_new_file(directory + "/artikel.doc")
            fungsi.write_to_file(directory + "/artikel.doc", article_format)
            print(article_format)

get_detail("https://www.niagahoster.co.id/blog/cara-membuat-website/", "Tutorial")
