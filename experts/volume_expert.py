from experts.base import ExpertOpinion


class VolumeExpert:

    def evaluate(self, df):

        row = df.iloc[-1]

        score = 0

        reasons = []

        if row["VOL_RATIO"] > 2:

            score += 40

            reasons.append("出来高2倍")

        if row["OBV"] > df["OBV"].iloc[-5]:

            score += 20

            reasons.append("OBV上昇")

        if row["High"] >= row["HIGH20"]:

            score += 20

            reasons.append("高値更新")

        if row["Close"] > row["BB_UPPER"]:

            score += 20

            reasons.append("ブレイクアウト")

        action = "BUY"

        if score < 60:
            action = "HOLD"

        if score < 30:
            action = "SELL"

        return ExpertOpinion(
            "Volume",
            score,
            action,
            reasons
        )