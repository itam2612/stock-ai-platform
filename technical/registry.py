class IndicatorRegistry:

    def __init__(self):
        self._indicators = []

    def register(self, indicator):
        self._indicators.append(indicator)

    def get_all(self):
        return self._indicators