from pathlib import Path

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"

STOCK_DIR = DATA_DIR / "stock"

ZIP_FILE = DATA_DIR / "stock.zip"

LOG_DIR = BASE_DIR / "logs"

REPORT_DIR = BASE_DIR / "report"

START_DATE = "2000-01-01"

END_DATE = "2030-01-01"

BUY_SCORE = 80

SELL_SCORE = 30