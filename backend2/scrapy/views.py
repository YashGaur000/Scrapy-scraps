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
        return f"{self.title}{self.price}{self.url}{self.image}{self.desc}"


header_flipkart = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
}
header_amazon = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1"
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
    try:
        web_url = "https://www.flipkart.com"
        base_url = "https://www.flipkart.com/search?q="
        url = base_url + product_name
        data = requests.get(url, headers=header_flipkart)
        soup = BeautifulSoup(data.content, 'lxml')
        print(data.content)
        mobile_titles = soup.find_all("div", {"class": "_4rR01T"})
        prices = soup.find_all("div", {"class": ["_30jeq3", "_1_WHN1"]})
        image_srcs_div = soup.find_all("div", {"class": "CXW8mj"})
        product_links = soup.find_all("a", {"class": "_1fQZEK"})
        for mobile_title, mobile_price, image_src_div, product in zip(mobile_titles, prices, image_srcs_div,
                                                                      product_links):
            url = product["href"]
            print(url)
            product_url = base_url + url
            image = image_src_div.find("img")
            image_src = image["src"]
            title = mobile_title.text
            price = mobile_price.text

            break
        return title, price, image_src, product_url
    except Exception:
        title = "None"
        price = "None"
        image_src = "None"
        product_url = "None"
        return title, price, image_src, product_url

def fetch_amazon_product_desc(url):
    data = requests.get(url, headers=header_amazon)
    soup = BeautifulSoup(data.content, 'lxml')


def fetch_amazon_data(product_name):
    try:
        base_url = "https://www.amazon.in"
        url = "https://www.amazon.in/s?k=" + product_name
        data = requests.get(url, headers=header_amazon)
        # print("Response is : ", data.content)
        soup = BeautifulSoup(data.content, 'lxml')
        image_div = soup.find("img", {"class": "s-image"})
        src = image_div["src"]
        # print(src)
        get_div = soup.find("div", attrs={"class": "sg-col-inner"})

        mobile_titles = get_div.find_all("span", {"class": ["a-color-state", "a-text-bold"]})
        product_urls_h2 = soup.find_all("h2",
                                        {"class": ["a-size-mini", "a-spacing_none", "a-color-base", "s-line-clamp-2"]})

        # complete_url = base_url + product_url["href"]
        prices = soup.find_all("span", {"class": "a-price-whole"})
        # print(prices)
        for mobile_title, mobile_price, product_url_h2 in zip(mobile_titles, prices, product_urls_h2):
            product_url = product_url_h2.a["href"]
            complete_url = base_url + product_url
            title = mobile_title.text
            price = mobile_price.text

            break
        desc = fetch_amazon_product_desc(url=complete_url)
        return title, price, src, complete_url
    except Exception:
        title = "None"
        price = "None"
        src = "None"
        complete_url = "None"
        return title, price, src, product_url


class DisplayData(APIView):

    ## This is currently for testing
    def get(self, request):
        product_name = "HONOR 90 (Diamond Silver, 8GB + 256GB)"

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
                    "Product_name": amazon.title,
                    "price": amazon.price,
                    "ImageUrl": amazon.image,
                    "Product_Url": amazon.url,
                },
                "flipkart": {
                    "Product_name": flipkart.title,
                    "price": flipkart.price,
                    "ImageUrl": flipkart.image,
                    "Product_Url": flipkart.url
                }
            })

    # This is not working at this moment will be implemented later
    def post(self, request):
        product_name = request.POST["product-name"]
        amazon_title, amazon_price = fetch_amazon_data(product_name)
        flipkart_title, flipkart_price, image_src = fetch_flipkart_data(product_name)
        return Response({
            "Amazon": {"title": amazon_title, "price": amazon_price},
            "Flipkart": {"title": flipkart_title, "price": flipkart_price, "img src": image_src}
        })
