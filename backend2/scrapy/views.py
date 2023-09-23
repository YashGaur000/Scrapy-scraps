import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import APIView
from rest_framework.response import Response


class MarketPlace:
    def __int__(self, title, image, url, price, desc):
        self.title = title
        self.image = image
        self.url = url
        self.price = price
        self.desc = desc

    def __repr__(self):
        print(f"{self.title}{self.price}{self.url}{self.image}{self.desc}")


Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
}

products = [
    "Samsung 236L 3 Star Digital Inverter Frost-Free Double Door Refrigerator (RT28C3053S8/HL,Elegant Inox , 2023 Model)",
    "Samsung Galaxy Z Fold5 5G (Cream, 12GB RAM, 512GB Storage)",
    "Apple iPhone 15 Plus (128 GB) - Blue",
    "HONOR 90 (Diamond Silver, 8GB + 256GB) | India's First Eye Risk-Free Display | 200MP Main & 50MP Selfie Camera | Segment First Quad-Curved AMOLED Screen | Without Charger"
]

amazon = MarketPlace()
flipkart = MarketPlace()
croma = MarketPlace()

def fetch_flipkart_data(product_name):
    base_url = "https://www.flipkart.com/search?q="
    url = base_url + product_name
    data = requests.get(url, headers=Headers)
    soup = BeautifulSoup(data.content, 'lxml')
    mobile_titles = soup.find_all("div", {"class": "_4rR01T"})
    prices = soup.find_all("div", {"class": ["_30jeq3", "_1_WHN1"]})

    image_srcs_div = soup.find_all("div", {"class": "CXW8mj"})
    product_links = soup.find_all("a", {"class": "_1fQZEK"})
    for mobile_title, mobile_price, image_src_div, product in zip(mobile_titles, prices, image_srcs_div, product_links):
        url = product["href"]
        product_url = base_url + url
        image = image_src_div.find("img")
        image_src = image["src"]
        title = mobile_title.text
        price = mobile_price.text

        break
    return title, price, image_src, product_url


def fetch_amazon_data(product_name):
    base_url = "https://www.amazon.in"
    url = "https://www.amazon.in/s?k=" + product_name
    data = requests.get(url, headers=Headers)
    soup = BeautifulSoup(data.content, 'lxml')
    image_div = soup.find("img", {"class": "s-image"})
    src = image_div["src"]
    # print(src)
    get_div = soup.find("div", attrs={"class": "sg-col-inner"})

    mobile_titles = get_div.find_all("span", {"class": ["a-color-state", "a-text-bold"]})
    product_url = soup.find("a", attrs={"class": ["a-link-normal", "s-underline-text", "s-underline-link-text"]})
    url = product_url["href"]
    complete_url = base_url + url
    prices = soup.find_all("span", {"class": "a-price-whole"})
    # print(prices)
    for mobile_title, mobile_price in zip(mobile_titles, prices):
        title = mobile_title.text
        price = mobile_price.text

        break

    return title, price, src, complete_url

class DisplayData(APIView):

## This is currently for testing
    def get(self, request):
        product_name = "Apple iPhone 15 Plus (128 GB) - Blue"
        try:
            amazon.title, amazon.price, amazon.image, amazon.url = fetch_amazon_data(product_name)
            flipkart.title, flipkart.price, flipkart.image, flipkart.url = fetch_flipkart_data(product_name)

        except:
            return Response({
                "status": 404
            })

        else:
            return Response({
                "status": 200,
                "amazon": {
                 "title": amazon.title,
                 "price": amazon.price,
                 "image": amazon.image,
                 "url": amazon.url,
                },
                "flipkart": {
                 "title": flipkart.title,
                 "price": flipkart.price,
                 "image": flipkart.image,
                 "url": flipkart.url
                }
            })

# This is not working at this moment will be implemented later
    def post(self, request):
        product_name = request.POST["product-name"]
        amazon_title, amazon_price = fetch_amazon_data(product_name)
        # flipkart_title, flipkart_price, image_src = fetch_flipkart_data(product_name)
        return Response({
            "Amazon": {"title": amazon_title, "price": amazon_price},
            # "Flipkart": {"title": flipkart_title, "price": flipkart_price, "img src": image_src}
        })
