import pandas as pd
from pathlib import Path

from config import STOCK_DIR


class StockLoader:

    def __init__(self):

        self.stocks = {}

    def load(self):

        files = sorted(STOCK_DIR.glob("*.xlsx"))

        for file in files:

            code = file.stem

            df = pd.read_excel(file)

            df["Date"] = pd.to_datetime(df["Date"])

            df.sort_values("Date", inplace=True)

            df.reset_index(drop=True, inplace=True)

            self.stocks[code] = df

        return self.stocks