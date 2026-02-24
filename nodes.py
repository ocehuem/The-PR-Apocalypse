import json
from langchain_groq import ChatGroq
from prompts import EVENT_PROMPT, CONSEQUENCE_PROMPT
from game_state import GameState
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()
class Consequence(BaseModel):
    reputation_delta: int
    cash_delta: int
    morale_delta: int
    narration: str


llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0.7)


def generate_event(state: GameState) -> GameState:
    response = llm.invoke(EVENT_PROMPT)
    state["current_event"] = response.content.strip()
    return state


def player_choice(state: GameState) -> GameState:
    print("\n==============================")
    print(f"ROUND {state['round']}")
    print(f"Reputation: {state['reputation']}")
    print(f"Cash: {state['cash']}")
    print(f"Morale: {state['morale']}")
    print("\nCrisis Event:")
    print(state["current_event"])

    print("\nWhat will you do:")


    choice = input("Enter :").strip()
    state["last_choice"] = choice

    return state


def llm_consequence(state: GameState) -> GameState:

    prompt = CONSEQUENCE_PROMPT.format(
        reputation=state["reputation"],
        cash=state["cash"],
        morale=state["morale"],
        event=state["current_event"],
        choice=state["last_choice"]
    )

    response = llm.invoke(prompt)
    content = response.content.strip()

    if content.startswith("```"):
        content = content.split("```")[1]

    try:
        data = json.loads(content)
    except Exception:
        print("\nInvalid JSON from model. Ending game.")
        state["next_step"] = "end"
        return state

    # New absolute values from model
    new_rep = data.get("reputation", state["reputation"])
    new_cash = data.get("cash", state["cash"])
    new_morale = data.get("morale", state["morale"])

    # Compute deltas
    state["reputation_delta"] = new_rep - state["reputation"]
    state["cash_delta"] = new_cash - state["cash"]
    state["morale_delta"] = new_morale - state["morale"]

    state["narration"] = data.get("narration", "")

    return state

def update_state(state: GameState) -> GameState:

    def clamp_stat(x):
        return max(0, min(100, x))

    # Apply deltas
    state["reputation"] = clamp_stat(
        state["reputation"] + state["reputation_delta"]
    )
    state["cash"] = clamp_stat(
        state["cash"] + state["cash_delta"]
    )
    state["morale"] = clamp_stat(
        state["morale"] + state["morale_delta"]
    )

    state["history"].append(state["narration"])
    state["round"] += 1

    print("\nOutcome:")
    print(state["narration"])

    print("\nNew Stats:")
    print(f"Reputation: {state['reputation']}")
    print(f"Cash: {state['cash']}")
    print(f"Morale: {state['morale']}")

    return state


def check_status(state: GameState) -> GameState:
    if (
        state["reputation"] <= 0
        or state["cash"] <= 0
        or state["morale"] <= 0
    ):
        print("\nYou collapsed under pressure.")
        state["next_step"] = "end"
        return state

    if state["round"] > 5:
        print("\nYou survived the crisis. You win.")
        state["next_step"] = "end"
        return state

    state["next_step"] = "generate_event"
    return state



