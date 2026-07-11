import zipfile

from config import ZIP_FILE
from config import STOCK_DIR


def unzip_stock():

    if STOCK_DIR.exists():
        return

    STOCK_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(ZIP_FILE, "r") as z:
        z.extractall(STOCK_DIR.parent)

    print("ZIPを解凍しました")