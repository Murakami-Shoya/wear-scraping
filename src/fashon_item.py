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
        
        # 「ブランド:」というテキストを含むspanタグを探す
        brand_span = self.soup.find('span', text='ブランド:')
        if brand_span:
            # 見つかったspanタグの次のaタグを取得
            brand_link = brand_span.find_next('a')
            
            if brand_link:
                return brand_link.text
        return None

    def save_fist_img(self):
        img = self.soup.find('img')
        if img:
            # 画像をダウンロード
            img_url = img['src']
            img_response = requests.get(img_url)
            with open(f"fashion_images/{self.img_filename}", 'wb') as f:
                f.write(img_response.content)
            return self.img_filename
        return None
    
    def get_category(self):
        category_list = []
        for category in self.soup.find('dt', text='カテゴリー').find_next('dd').find_all('a'):
            category_list.append(category.text)
        return category_list

    def get_keyword(self):
        keyword_list = []
        for keyword in self.soup.find('dt', text='キーワード').find_next('dd').find_all('a'):
            keyword_list.append(keyword.text)
        return keyword_list

    def get_explain(self):
        self.explain = self.soup.find('h2', text='アイテム説明').find_next('p').text
        return self.explain
    
    def get_coordinate(self):
        coordinate_url_list = []
        for coordinate in self.soup.find(text='着用コーディネート').find_next('ul').find_all('a'):
            coordinate_url_list.append(coordinate['href'])
        return coordinate_url_list