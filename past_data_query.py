from query_stock import QueryStock
from datetime import datetime, timedelta

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2021-01-01", "2021-01-09")
print(dates)

if __name__ == "__main__":
    query_stock = QueryStock()
    for dates in date_range("2022-01-01", "2023-09-10"):
        weekday = datetime.strptime(dates, "%Y-%m-%d").weekday()
        print(weekday)
        if weekday != 5 and weekday != 6:
            dates = dates.replace("-", "")
            df = query_stock.query_stock("xml", "KOSDAQ", "1673", "1", dates)
            df = query_stock.query_stock("xml", "KOSPI", "1673", "1", dates)
    """query_stock = QueryStock()
    df = query_stock.query_stock("xml", "KOSDAQ", "1673", "1", "20211114")
    df.show()
    print(df.count())
    df = query_stock.query_stock("xml", "KOSPI", "1673", "1", "20211114")
    df.show()
    print(df.count())"""