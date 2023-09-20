from pyspark.sql import SparkSession
from os.path import exists
from shutil import rmtree

class SaveStockData:
    def __init__(self, info_list:list, dir_name:str, mrkt_cls:str):
        self.spark = SparkSession.builder.appName("stock_info").getOrCreate()
        self.info_list = info_list
        self.dir_name = dir_name
        self.mrkt_cls = mrkt_cls
    
    def _convert_to_rdd(self):
        return self.spark.sparkContext.parallelize(self.info_list)
    
    def _convert_to_df(self, rdd):
        return self.spark.read.json(rdd)
    
    def _check_output_dir(self):
        if exists(f"./{self.mrkt_cls}_{self.dir_name}"):
            rmtree(f"./{self.mrkt_cls}_{self.dir_name}")

    def _save_as_text(self, df):
        #df.toJSON().saveAsTextFile(f"./{self.mrkt_cls}_{self.dir_name}")
        df.write.json(f"./{self.mrkt_cls}_{self.dir_name}")

    def save_stock_data(self):
        rdd = self._convert_to_rdd()
        df = self._convert_to_df(rdd)
        df.show()
        self._check_output_dir()
        self._save_as_text(df)
        return df
