from dataclasses import dataclass

@dataclass
class Position:

    code: str

    buy_date: str

    buy_price: float

    shares: int

    stop_loss: float

    take_profit: float