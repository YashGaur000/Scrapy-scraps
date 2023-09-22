import requests
from bs4 import BeautifulSoup
from rest_framework.decorators import APIView
from rest_framework.response import Response


Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
}

products = [
    "Samsung 236L 3 Star Digital Inverter Frost-Free Double Door Refrigerator (RT28C3053S8/HL,Elegant Inox , 2023 Model)",
    "Samsung Galaxy Z Fold5 5G (Cream, 12GB RAM, 512GB Storage)",
    "Apple iPhone 15 Plus (128 GB) - Blue",
    "HONOR 90 (Diamond Silver, 8GB + 256GB) | India's First Eye Risk-Free Display | 200MP Main & 50MP Selfie Camera | Segment First Quad-Curved AMOLED Screen | Without Charger"
]


def fetch_flipkart_data(product_name):
    data = requests.get("https://www.flipkart.com/search?q=" + product_name)
    soup = BeautifulSoup(data.content, 'lxml')
    mobile_titles = soup.find_all("div", {"class": "_4rR01T"})
    prices = soup.find_all("div", {"class": "_30jeq3 _1_WHN1"})
    for mobile_title, mobile_price in zip(mobile_titles, prices):
        title = mobile_title.text
        price = mobile_price.text
        return title, price

def fetch_amazon_data(product_name):
    url = "https://www.amazon.in/s?k=" + product_name
    data = requests.get(url, headers=Headers)
    soup = BeautifulSoup(data.content, 'lxml')
    get_div = soup.find("div", attrs={"class": "sg-col-inner"})
    print(get_div)
    mobile_titles = get_div.find_all("span", {"class": ["a-color-state", "a-text-bold"]})
    prices = soup.find_all("span", {"class": "a-price-whole"})
    for mobile_title, mobile_price in zip(mobile_titles, prices):
        title = mobile_title.text
        price = mobile_price.text
        return title, price


class DisplayData(APIView):

## This is currently for testing
    def get(self, request):
        product_name = "Apple iPhone 15 Plus (128 GB) - Blue"
        try:
            amazon_title, amazon_price = fetch_amazon_data(product_name)
            flipkart_title, flipkart_price = fetch_flipkart_data(product_name)

        except:
            return Response({
                "status": 404
            })

        else:
            return Response({
                "status": 200,
                "amazon_title": amazon_title,
                "amazon_price": amazon_price,
                "flipkart_price": flipkart_price,
                "flipkart_title": flipkart_title
            })

# This is not working at this moment will be implemented later
    def post(self, request):
        product_name = request.POST["product-name"]
        amazon_title, amazon_price = fetch_amazon_data(product_name)
        flipkart_title, flipkart_price = fetch_flipkart_data(product_name)
        return Response({
            "amazon_title": amazon_title,
            "amazon_price": amazon_price,
            "flipkart_price": flipkart_price,
            "flipkart_title": flipkart_title
        })
