from experts.base import ExpertOpinion


class MomentumExpert:

    def evaluate(self, df):

        row = df.iloc[-1]

        score = 0

        reasons = []

        if row["MACD"] > row["MACD_SIGNAL"]:

            score += 30

            reasons.append("MACD GC")

        if 40 < row["RSI"] < 70:

            score += 30

            reasons.append("RSI健全")

        if row["STOCH"] > row["STOCH_SIGNAL"]:

            score += 20

            reasons.append("ストキャスGC")

        if row["ROC"] > 0:

            score += 20

            reasons.append("ROCプラス")

        action = "BUY"

        if score < 60:
            action = "HOLD"

        if score < 30:
            action = "SELL"

        return ExpertOpinion(
            "Momentum",
            score,
            action,
            reasons
        )