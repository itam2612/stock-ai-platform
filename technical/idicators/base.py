from abc import ABC, abstractmethod
import pandas as pd


class BaseIndicator(ABC):
    """
    全テクニカル指標の親クラス
    """

    name = "Base"

    @abstractmethod
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        指標を計算してDataFrameへ追加する
        """
        pass