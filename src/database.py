import os
import pandas as pd

class DatabaseCSV():
    def __init__(self, filename):
        self.filename = filename
        if os.path.exists(filename):
            self.df = pd.read_csv(filename)
        else:

            self.df = pd.DataFrame(columns=['item_id', 
                                            'item_name', 
                                            'brand_name', 
                                            'category_list', 
                                            'keyword_list', 
                                            'explain', 
                                            'coordinate_url_list', 
                                            'img_filename', 
                                            'sex'])
    
    def add_data(self, fashion_item, sex):
        """
        アイテムをデータベースに追加する

        Parameters
        ----------
        fashion_item : FashionItem
            追加するアイテム

        Returns
        -------
        None（dfに追加）
        """
        # アイテム行を作成
        item_row = [fashion_item.item_id, 
                fashion_item.item_name, 
                fashion_item.brand_name, 
                fashion_item.category_list, 
                fashion_item.keyword, 
                fashion_item.explain, 
                fashion_item.coordinate_url_list, 
                fashion_item.img_filename,
                sex]

        item_id = int(fashion_item.item_id)
        # すでにデータベースに登録されている場合は追加しない
        if item_id not in self.df['item_id'].values:
            self.df.loc[len(self.df)] = item_row  # locを使用して行を追加
            
            # 保存
            self.df.to_csv(self.filename, index=False, encoding='utf-8')

        



        