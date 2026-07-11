from experts.base import ExpertOpinion


class MarketExpert:

    def evaluate(self, df):

        score = 70

        return ExpertOpinion(

            "Market",

            score,

            "BUY",

            [

                "市場良好"

            ]
        )