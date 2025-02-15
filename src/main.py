from fashon_item import FashionItem

if __name__ == '__main__':
    # ファッションアイテムのURL
    url = 'https://wear.jp/item/82875692/'
    # ファッションアイテムのスクレイピング
    fashion_item = FashionItem(url)

    # print(fashion_item.soup)
    print(fashion_item.item_name)
    print(fashion_item.brand_name)
    print(fashion_item.category_list)
    print(fashion_item.keyword)
    print(fashion_item.explain)
    print(fashion_item.coordinate_url_list)
    print(fashion_item.img_filename)