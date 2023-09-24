import unittest
from unittest.mock import patch
from django.test import Client


class TestMarketplaceAPI(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    @patch('scrapy.views.fetch_amazon_data')  # Replace 'your_module' with the actual module containing your code
    @patch('scrapy.views.fetch_flipkart_data')  # Replace 'your_module' with the actual module containing your code
    def test_marketplace_api(self, mock_fetch_amazon_data, mock_fetch_flipkart_data):
        self.maxDiff = None
        # Mock the return values of the scraping functions
        mock_fetch_amazon_data.return_value = (
            "HONOR 90 (Diamond Silver, 8GB 256GB)",
            "15,999.",
            "https://m.media-amazon.com/images/I/81ZmkhVU-RL._AC_UY218_.jpg",
            "https://www.amazon.in/sspa/click?ie=UTF8&spc=MToxMDgxNzc5NjE1MzYzMToxNjk1NTQ3MzU0OnNwX2F0ZjozMDAwNTc1NzI4ODkxMzI6OjA6Og&url=%2FMidnight-Risk-Free-Display-Segment-Quad-Curved%2Fdp%2FB0CG128DJK%2Fref%3Dsr_1_1_sspa%3Fkeywords%3DHONOR%2B90%2B%2528Diamond%2BSilver%252C%2B8GB%2B256GB%2529%26qid%3D1695547354%26sr%3D8-1-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9hdGY%26psc%3D1"
        )
        mock_fetch_flipkart_data.return_value = (
            "Honor 20i (Midnight Black, 128 GB)",
            "₹16,999",
            "https://rukminim2.flixcart.com/image/312/312/k2jbyq80pkrrdj/mobile-refurbished/p/r/v/20i-128-d-hry-al00ta-honor-4-original-imafgk2uybhgpzg4.jpeg?q=70",
            "https://www.flipkart.com/honor-20i-midnight-black-128-gb/p/itmfggkamk5q4y9x?pid=MOBFGGKAHWWT4HBV&lid=LSTMOBFGGKAHWWT4HBVDSCIS0&marketplace=FLIPKART&q=HONOR+90+%28Diamond+Silver%2C+8GB+256GB%29&store=tyy%2F4io&srno=s_1_1&otracker=search&fm=organic&iid=c31a2e80-a0ae-437b-9473-efbb080b1fd4.MOBFGGKAHWWT4HBV.SEARCH&ppt=None&ppn=None&ssid=y0cjm3r0k00000001695547359291&qH=ab9a0533ac5232c6"
        )

        # Make a POST request to your API endpoint with the desired product name
        response = self.client.post('/', {'product-name': 'HONOR 90 (Diamond Silver, 8GB 256GB)'})

        # Assert that the response status code is 200
        self.assertEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
