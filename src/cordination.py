import os
import requests
from bs4 import BeautifulSoup
from common import scrape_page

class Cordination:
    def __init__(self, url):
        self.soup = scrape_page(url)
        self.item_link_list = self.get_item_link_list()

    def get_item_link_list(self):
        item_link_list = []
        for item in self.soup.find(text='着用アイテム').find_next('ul').find_all('li'): # 着用アイテムのリストを取得
            item_link_list.append(f"https://wear.jp{item.find_next('a')['href']}")  # 着用アイテムのURLを取得
        return item_link_list

if __name__ == '__main__':
    # ファッションアイテムのURL
    url = 'https://wear.jp/akiiiio04/25015526/'

    # ファッションアイテムのスクレイピング
    cordination = Cordination(url)
    print(cordination.item_link_list)
        