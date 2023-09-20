from urllib import parse
from urllib.parse import urlencode

class GetURL:
    def __init__(self):
        
        self.base_url = f"http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={self.api_key}"
        self.params = {}

    def _get_result_type(self, result_type):
        self.params["resultType"] = result_type

    def _get_mrkt_cls(self, mrkt_cls):
        self.params["mrktCls"] = mrkt_cls

    def _get_num_of_rows(self, num_of_rows):
        self.params["numOfRows"] = num_of_rows

    def _get_page_no(self, page_no):
        self.params["pageNo"] = page_no

    def _get_bas_dt(self, bas_dt):
        self.params["basDt"] = bas_dt

    def _get_url(self):
        return self.base_url + "&" + urlencode(self.params)
    
    def get_url(self, result_type, mrkt_cls, num_of_rows, page_no, bas_dt):
        self._get_result_type(result_type)
        self._get_mrkt_cls(mrkt_cls)
        self._get_num_of_rows(num_of_rows)
        self._get_page_no(page_no)
        self._get_bas_dt(bas_dt)
        return self._get_url()
    
if __name__ == "__main__":
    query_url = GetURL()
    print(query_url.get_url("xml", "KOSDAQ", "1673", "1", "20190429"))
    print(query_url.get_url("json", "KOSDAQ", "1673", "1", "20190429"))
    print(query_url.get_url("xml", "KOSPI", "1673", "1", "20190429"))
    print(query_url.get_url("json", "KOSPI", "1673", "1", "20190429"))