from dataclasses import dataclass

@dataclass
class ExpertOpinion:

    name: str

    score: int

    action: str

    reasons: list