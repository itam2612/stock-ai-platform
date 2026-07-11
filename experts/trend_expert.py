from experts.base import ExpertOpinion


class TrendExpert:

    def evaluate(self, df):

        row = df.iloc[-1]

        score = 0

        reasons = []

        if row["SMA5"] > row["SMA25"]:

            score += 20

            reasons.append("SMA5>SMA25")

        if row["SMA25"] > row["SMA75"]:

            score += 20

            reasons.append("パーフェクトオーダー")

        if row["Close"] > row["SMA200"]:

            score += 20

            reasons.append("長期上昇")

        if row["ADX"] > 25:

            score += 20

            reasons.append("トレンド強")

        if row["Close"] > row["BB_MIDDLE"]:

            score += 20

            reasons.append("BB中央線上")

        action = "BUY"

        if score < 60:
            action = "HOLD"

        if score < 30:
            action = "SELL"

        return ExpertOpinion(
            "Trend",
            score,
            action,
            reasons
        )