import requests
from bs4 import BeautifulSoup


def fetch_data_and_save_to_file(url, path):
    data = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(data.text)


url = "https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_3_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_3_0_na_na_na&as-pos=3&as-type=TRENDING&suggestionId=mobiles&requestId=90c188d0-bf6a-4593-b462-f5fdb8d0fa73"
file_name = "mobiles.html"
fetch_data_and_save_to_file(url, file_name)
with open(file_name, "r", encoding="utf-8") as f:
    html_doc = f.read()
soup = BeautifulSoup(html_doc, "html.parser")
mobile_titles = soup.find_all("div", {"class": "_4rR01T"})
prices = soup.find_all("div", {"class": "_30jeq3 _1_WHN1"})
for mobile_title, mobile_price in zip(mobile_titles, prices):
    title = mobile_title.text
    price = mobile_price.text
    print(title, price)
