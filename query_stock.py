from data_pipeline.get_url import GetURL
from data_pipeline.get_contents import GetContents
from data_pipeline.save_stock_data import SaveStockData
from data_pipeline.read_stock_data import ReadStockData

class QueryStock:
    def __init__(self):
        self.query_url = GetURL()
    
    def query_stock(self, result_type, mrkt_cls, num_of_rows, page_no, bas_dt):
        url = self.query_url.get_url(result_type, mrkt_cls, num_of_rows, page_no, bas_dt)
        query_contents = GetContents(url).get_contents()
        save_stock_data = SaveStockData(query_contents, bas_dt, mrkt_cls).save_stock_data()
        read_stock_data = ReadStockData(f"./{mrkt_cls}_{bas_dt}").read_stock_data()
        return read_stock_data
    

