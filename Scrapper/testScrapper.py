import requests
import unittest
from bs4 import BeautifulSoup

class TestScrapper(unittest.TestCase):
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.46'}
    URL = 'https://fr.indeed.com/jobs?q=d%C3%A9veloppeur%20python&l=Paris%20(75)&radius=10&start=0'
    r = requests.get(URL, headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    def test_1_connection_to_website(self):
        r = requests.get(TestScrapper.URL)
        self.assertEqual(r.status_code, 200)

    def test_2_content_exist(self):
        content = TestScrapper.soup.find('h2', class_='jobTitle')
        self.assertIsNotNone(content)

    def test_3_titleText(self):
        baliseTitle = TestScrapper.soup.find('h2', class_='jobTitle').get_text()
        print(baliseTitle)
        self.assertEqual('nouveauDéveloppeur(euse) PYTHON', baliseTitle)




