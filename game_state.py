from typing import TypedDict, List


class GameState(TypedDict):
    reputation: int
    cash: int
    morale: int
    round: int
    history: List[str]
    current_event: str
    last_choice: str
    reputation_delta: int
    cash_delta: int
    morale_delta: int
    narration: str
    next_step: str