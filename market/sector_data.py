class DataChecker:

    def check(self, stocks):

        print("==== Data Summary ====")

        print("銘柄数:", len(stocks))

        for code, df in list(stocks.items())[:5]:

            print()

            print(code)

            print(df.head())

            print(df.columns)

            print(df.isna().sum())