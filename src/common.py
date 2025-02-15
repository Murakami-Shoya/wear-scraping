import requests
from bs4 import BeautifulSoup

def scrape_page(base_url):
    # ページへのリクエスト
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup