import os
import requests
from common import scrape_page

class FashionItem:
    def __init__(self, url, pre_scrape=True):
        self.item_id = url.split('/')[-2]
        if pre_scrape:
            self.soup = scrape_page(url)
            self.item_name = self.soup.find('h1').text
            self.brand_name = self.get_brand_name()
            self.category_list = self.get_category()
            self.keyword = self.get_keyword()
            self.explain = self.get_explain()
            self.coordinate_url_list = self.get_coordinate()
            self.img_filename = f'wear_{self.item_id}.jpg'    # 画像ファイル名
        else:
            self.soup = None
            self.item_name = None
            self.brand_name = None
            self.category_list = None
            self.keyword = None
            self.explain = None
            self.coordinate_url_list = None
            self.img_filename = None

    def get_brand_name(self):
        try:
            brand_link = self.soup.find('span', text='ブランド:').find_next('a')
            return brand_link.text if brand_link else None
        except AttributeError:
            return None

    def save_fist_img(self):
        try:
            img_url = self.soup.find('img')['src']
            img_response = requests.get(img_url)
            with open(f"fashion_images/{self.img_filename}", 'wb') as f:
                f.write(img_response.content)
            return self.img_filename
        except (AttributeError, KeyError, requests.RequestException):
            return None
    
    def get_category(self):
        try:
            return [category.text for category in self.soup.find('dt', text='カテゴリー').find_next('dd').find_all('a')]
        except AttributeError:
            return None

    def get_keyword(self):
        try:
            return [keyword.text for keyword in self.soup.find('dt', text='キーワード').find_next('dd').find_all('a')]
        except AttributeError:
            return None

    def get_explain(self):
        try:
            # 不要な改行（\t\n\r\f\v）を削除
            return self.soup.find('h2', text='アイテム説明').find_next('p').text.replace('\n', '').replace('\t', '').replace('\r', '').replace('\f', '').replace('\v', '').replace('\u3000', '')
        except AttributeError:
            return None
    
    def get_coordinate(self):
        try:
            return [coordinate['href'] for coordinate in self.soup.find(text='着用コーディネート').find_next('ul').find_all('a')]
        except AttributeError:
            return None
        
if __name__ == '__main__':
    # ファッションアイテムのURL
    url = 'https://wear.jp/item/85859447/'

    # ファッションアイテムのスクレイピング
    fashion_item = FashionItem(url)
    print(fashion_item.item_name)
    print(fashion_item.brand_name)
    print(fashion_item.category_list)
    print(fashion_item.keyword)
    print(fashion_item.explain)
    print(fashion_item.coordinate_url_list)
    print(fashion_item.img_filename)
    fashion_item.save_fist_img()