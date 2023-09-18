import requests
from bs4 import BeautifulSoup

baseURL = "https://www.flipkart.com/"

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59'
}


productlinks = []
for x in range (1,6):
    r = requests.get(f"https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=c3b79e99-6b4f-4c77-8c28-ed671b5e964d&as-backfill=on&page={x}")
    soup = BeautifulSoup(r.content, 'lxml')

    mobiles=(soup.find('div', class_='_4rR01T').text)
    price=(soup.find('div', class_='_30jeq3 _1_WHN1').text)

mobile_details = {
    'mobile': mobiles,
    'price': price
}

print(mobile_details)   #output => {'mobile': 'SAMSUNG Galaxy M33 5G (Mystique Green, 128 GB)', 'price': '₹16,989'}

    # pricelist=soup.find_all('div', class_='_30jeq3 _1_WHN1')

    # print(productlist)
    # print(pricelist)


#     for item in productlist:
#         # for link in item.find_all('a', href=True):
#         productlinks.append(item)

# print(productlinks)    #number of items per page
