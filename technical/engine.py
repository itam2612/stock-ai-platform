from tqdm import tqdm

from technical.indicators import IndicatorCalculator


class IndicatorEngine:

    def calculate(self, stocks):

        result = {}

        print("Indicator計算開始")

        for code in tqdm(stocks):

            df = stocks[code]

            df = IndicatorCalculator.add_all(df)

            result[code] = df

        print("Indicator計算終了")

        return result