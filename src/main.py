import os
import time  # timeモジュールをインポート
from common import scrape_page
from database import DatabaseCSV

from fashon_item import FashionItem
from cordination import Cordination

if __name__ == '__main__':
    # ファッションアイテムのURL
    page_num = 1
    sex = 'women'
    url = f'https://wear.jp/{sex}-coordinate/?pageno={page_num}'

    db = DatabaseCSV('fashion_item.csv')

    # 保存用のディレクトリ作成
    if not os.path.exists('fashion_images'):
        os.makedirs('fashion_images')
    # ファッションアイテムのスクレイピング
    # コーディネートランキング→コーディネート→アイテムでスクレイピング
    soup = scrape_page(url)
    for a in soup.find_all('a', class_='relative'): # class_='relative'のaタグがコーディネートのリンク
        print(f"コーディネート：https://wear.jp{a['href']}")
        coordination = Cordination(f"https://wear.jp{a['href']}")

        print(len(coordination.item_link_list))
        for item_link in coordination.item_link_list:
            print(f"アイテム：{item_link}")
            fashion_item = FashionItem(item_link)
            db.add_data(fashion_item, sex)
            fashion_item.save_fist_img()
            time.sleep(1)  # 各アイテムの処理後に1秒待機
