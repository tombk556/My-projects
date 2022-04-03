from data_extraction import Extraction
import pandas as pd 


class Store(Extraction):
    
    def __init__(self, stock_dict: dict):
            self.stock_dict = stock_dict
            
    def fetch_and_store(self):
        for stock in self.stock_dict:
            stock_data = Extraction(self.stock_dict[stock]
                                    ,stock,
                                    2015, 1, 1)
            
            stock_data = stock_data.extract_data()
            stock_data.to_csv(f'./Raw_Data/{stock}.csv')
            
