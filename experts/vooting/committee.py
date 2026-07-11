from experts.trend_expert import TrendExpert
from experts.momentum_expert import MomentumExpert
from experts.volume_expert import VolumeExpert
from experts.market_expert import MarketExpert


class Committee:

    def __init__(self):

        self.experts = [

            TrendExpert(),

            MomentumExpert(),

            VolumeExpert(),

            MarketExpert()

        ]

    def evaluate(self, df):

        opinions = []

        total = 0

        for expert in self.experts:

            op = expert.evaluate(df)

            opinions.append(op)

            total += op.score

        avg = total / len(opinions)

        decision = "HOLD"

        if avg >= 80:

            decision = "STRONG BUY"

        elif avg >= 65:

            decision = "BUY"

        elif avg >= 50:

            decision = "WATCH"

        elif avg < 30:

            decision = "SELL"

        return {

            "score": avg,

            "decision": decision,

            "opinions": opinions

        }