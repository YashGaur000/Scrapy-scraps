from bs4 import BeautifulSoup
import requests


def fetch_data_and_save_to_file(url, path):
    data = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(data.text)


url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
fetch_data_and_save_to_file(url, "book.html")
with open("book.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, "html.parser")
articles = soup.find_all("article", {"class": "product_pod"})

for article in articles:
    book_title = article.find("h3").text
    print(book_title)
