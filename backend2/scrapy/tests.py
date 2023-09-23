from django.test import TestCase
from unittest.mock import patch
from scrapy.views import DisplayData

class DisplayDataTestCase(TestCase):
    @patch('scrapy.views.fetch_amazon_data')
    @patch('scrapy.views.fetch_flipkart_data')
    def test_display_data_success(self, mock_fetch_flipkart_data, mock_fetch_amazon_data):
        # Mock the fetch_amazon_data and fetch_flipkart_data functions
        mock_fetch_amazon_data.return_value = {
            "title": "Amazon Product Title",
            "price": 100.00,
            "image": "amazon_image_url",
            "url": "amazon_product_url",
        }
        mock_fetch_flipkart_data.return_value = {
            "title": "Flipkart Product Title",
            "price": 90.00,
            "image": "flipkart_image_url",
            "url": "flipkart_product_url",
        }

        # Make a GET request to the view
        response = self.client.get('/your-api-url/')

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check the content of the response
        expected_response = {
            "status": 200,
            "amazon": {
                "title": "Amazon Product Title",
                "price": 100.00,
                "image": "amazon_image_url",
                "url": "amazon_product_url",
            },
            "flipkart": {
                "title": "Flipkart Product Title",
                "price": 90.00,
                "image": "flipkart_image_url",
                "url": "flipkart_product_url",
            }
        }
        self.assertEqual(response.data, expected_response)

    @patch('scrapy.views.fetch_amazon_data')
    @patch('scrapy.views.fetch_flipkart_data')
    def test_display_data_failure(self, mock_fetch_flipkart_data, mock_fetch_amazon_data):
        # Mock the fetch_amazon_data and fetch_flipkart_data functions to raise an exception
        mock_fetch_amazon_data.side_effect = Exception("Amazon Error")
        mock_fetch_flipkart_data.side_effect = Exception("Flipkart Error")

        # Make a GET request to the view
        response = self.client.get('/your-api-url/')

        # Check that the response status code is 404
        self.assertEqual(response.status_code, 404)
