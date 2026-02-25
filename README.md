# The PR Apocalypse

**The PR Apocalypse** is an LLM-powered corporate crisis simulation built with LangGraph and Groq.

- The game loop is built using **LangGraph's StateGraph**, which enables structured, stateful execution between nodes.

- LLM used for event + consequence generation

Navigate escalating PR disasters. Make high-stakes executive decisions.  
Control the narrative before the narrative controls you.


---

### Nodes

- `generate_event` → Creates new crisis scenario
- `player_choice` → Captures player decision
- `llm_consequence` → LLM calculates impact
- `update_state` → Applies numerical deltas
- `check_status` → Determines continuation or termination


---

## Execution Flow

```
generate_event
      ↓
player_choice
      ↓
llm_consequence
      ↓
update_state
      ↓
check_status
      ↓
(generate_event OR END)
```

---

## Tech Stack

- Python 3.10+
- Groq API
- LangChain
- LangGraph
- Pydantic
- python-dotenv
- uv (dependency management)

---

## Development Environment

- IDE: PyCharm/vscode
- Shell: Git Bash
- Dependency Manager: uv

---

## Installation & Setup

Download pycharm IDE

### 1. Clone the repository

```bash
git clone https://github.com/ocehuem/The-PR-Apocalypse.git
cd The-PR-Apocalypse
```

### 2. Initialize project (only if starting fresh)

In GitBash:

```bash
uv init
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Add environment variables

Create a `.env` file in the root directory or add api key in the nodes.py in the space given 

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the game

just press run in the IDE for main.py
