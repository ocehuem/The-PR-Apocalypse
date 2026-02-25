import os
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from game_state import GameState
from nodes import (
    generate_event,
    player_choice,
    llm_consequence,
    update_state,
    check_status,
)

load_dotenv()

initial_state: GameState = {
    "reputation": 50,
    "cash": 50,
    "morale": 50,
    "round": 1,
    "history": [],
    "current_event": "",
    "last_choice": "",
    "narration": "",
    "next_step": "generate_event",
}


builder = StateGraph(GameState)

builder.add_node("generate_event", generate_event)
builder.add_node("player_choice", player_choice)
builder.add_node("llm_consequence", llm_consequence)
builder.add_node("update_state", update_state)
builder.add_node("check_status", check_status)

builder.set_entry_point("generate_event")

builder.add_edge("generate_event", "player_choice")
builder.add_edge("player_choice", "llm_consequence")
builder.add_edge("llm_consequence", "update_state")
builder.add_edge("update_state", "check_status")

builder.add_conditional_edges(
    "check_status",
    lambda state: state["next_step"],
    {
        "generate_event": "generate_event",
        "end": END,
    },
)

graph = builder.compile()

if __name__ == "__main__":
    graph.invoke(initial_state)