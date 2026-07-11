from utils.unzip import unzip_stock
from utils.loader import StockLoader
from utils.checker import DataChecker

print("StockAI")

print("Phase1")

unzip_stock()

loader = StockLoader()

stocks = loader.load()

checker = DataChecker()

checker.check(stocks)

print("終了")

from technical.engine import IndicatorEngine

engine = IndicatorEngine()

stocks = engine.calculate(stocks)


from voting.committee import Committee

committee = Committee()

result = committee.evaluate(

    stocks["7203"]

)

print(result)