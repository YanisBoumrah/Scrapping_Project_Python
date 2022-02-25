import requests
import unittest
from bs4 import BeautifulSoup

class TestScrapper(unittest.TestCase):

    URL = 'https://fr.indeed.com/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')

    def test_1_connection_to_website(self):
        r = requests.get(TestScrapper.URL)
        self.assertEqual(r.status_code, 200)

    def test_2_content_exist(self):
        content = TestScrapper.soup.find('h2', {'class':'jobTitle jobTitle-newJob'}).get_text()
        print(content)


    def test_3_text_exist(self):
        content = TestScrapper.soup.findAll


