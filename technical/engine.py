from technical.registry import IndicatorRegistry


class TechnicalEngine:

    def __init__(self):

        self.registry = IndicatorRegistry()

    def add_indicator(self, indicator):

        self.registry.register(indicator)

    def calculate(self, df):

        for indicator in self.registry.get_all():

            df = indicator.calculate(df)

        return df