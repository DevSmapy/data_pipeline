from glob import glob
from pyspark.sql import SparkSession

class ReadStockData:
    def __init__(self, data_path):
        self.data_list = sorted(glob(data_path + "/part-*"))
        self.spark = SparkSession.builder.appName("stock_info").getOrCreate()

    def _read_data(self, file_name):
        return self.spark.read.json(file_name)
    
    def _check_dataframe(self, df):
        if df.toPandas().empty:
            return False
        else:
            return True
    
    def _union_data(self, df1, df2):
        empty_df1 = self._check_dataframe(df1)
        empty_df2 = self._check_dataframe(df2)
        if empty_df1 and empty_df2:
            return df1.union(df2)
        elif empty_df1 and not empty_df2:
            return df1
        elif not empty_df1 and empty_df2:
            return df2
        else:
            return None
    
    def _get_data(self):
        df = self._read_data(self.data_list[0])
        for file_name in self.data_list[1:]:
            df = self._union_data(df, self._read_data(file_name))
        return df
    
    def read_stock_data(self):
        return self._get_data()
    
