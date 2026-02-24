# The PR Apocalypse

**The PR Apocalypse** is an LLM-powered corporate crisis simulation built with LangGraph and Groq.

Navigate escalating PR disasters. Make high-stakes executive decisions.  
Control the narrative before the narrative controls you.

Stateful event escalation • Decision branching • Reputation dynamics

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

- IDE: PyCharm
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

```bash
uv init
```

### 3. Install dependencies

```bash
uv sync
```

### 4. Add environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run the game

```bash
uv run python main.py
```

---

## What This Project Demonstrates

- Stateful AI game design
- Structured prompt engineering
- LangGraph workflow orchestration
- LLM-driven narrative simulation
- Decision-impact modeling

---

## License

MIT
