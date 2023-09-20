from query_stock import QueryStock

if __name__ == "__main__":
    query_stock = QueryStock()
    #df = query_stock.query_stock("xml", "KOSDAQ", "1673", "1", "20220103")
    #df.show()
    #print(df.count())
    df = query_stock.query_stock("xml", "KOSPI", "1673", "1", "20230908")
    df.show()
    print(df.count())
