import time
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import os

class PriceData:


    def __init__(self):
        oneYearAgo = datetime.datetime.now() - relativedelta(days= 253)
        oneDayAgo = datetime.datetime.now() - relativedelta(days=1)
        self.period1 =  int(time.mktime(oneYearAgo.timetuple()))
        self.period2 = int(time.mktime(oneDayAgo.timetuple()))
        self.interval = "1d"

    def copyToCsv(self, path, ticker):
        query = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={self.period1}&period2={self.period2}&interval={self.interval}&events=history&includeAdjustedClose=true"
        df = pd.read_csv(query)
        # change column names to lowercase
        df.columns = map(str.lower, df.columns)
        # Add column symbol
        df["symbol"] = ticker

        if not os.path.isfile(path):
            df.to_csv(path, index=False)
        else:
            df.to_csv(path, index=False, mode="a", header=False)

# price = PriceData()
# print(price.copyToCsv("monte_carlo/data/stock_data_test7.csv", "AAPL"))