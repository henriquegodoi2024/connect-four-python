# connect-four-python
Python implementation of a Connect Four game with modular classes for the game board, players, game flow, and AI decision making. The project supports human input, random move selection, and lookahead based strategy for computer play

## What It Does

Two players take turns dropping checkers (`X` or `O`) into a 6×7 grid. The first player to connect four checkers in a row — horizontally, vertically, or diagonally — wins. The game supports three player types that can be mixed and matched:

| Player Type | Description |
|---|---|
| `Player` | Human — prompted to enter a column number each turn |
| `RandomPlayer` | Computer — picks a valid column at random |
| `AIPlayer` | Computer — uses minimax lookahead to choose the best move |

---

## Project Structure

| File | Responsibility |
|---|---|
| `checker1.py` | `Board` class — the game grid, win detection, checker placement |
| `checker2.py` | `Player` class — human player with input handling |
| `checker3.py` | `RandomPlayer` class + `connect_four()` game loop |
| `checker4.py` | `AIPlayer` class — minimax AI with tiebreaking strategies |

---

## Quickstart

### Human vs Human
```python
from checker3 import connect_four
from checker2 import Player

p1 = Player('X')
p2 = Player('O')
connect_four(p1, p2)
```

### Human vs Random Computer
```python
from checker3 import connect_four, RandomPlayer
from checker2 import Player

p1 = Player('X')
p2 = RandomPlayer('O')
connect_four(p1, p2)
```

### Human vs AI
```python
from checker3 import connect_four
from checker2 import Player
from checker4 import AIPlayer

p1 = Player('X')
p2 = AIPlayer('O', 'LEFT', 3)   # tiebreak='LEFT', lookahead=3
connect_four(p1, p2)
```

### AI vs AI
```python
from checker3 import connect_four
from checker4 import AIPlayer

p1 = AIPlayer('X', 'RANDOM', 4)
p2 = AIPlayer('O', 'RIGHT', 4)
connect_four(p1, p2)
```

---

## AIPlayer Configuration

```python
AIPlayer(checker, tiebreak, lookahead)
```

**`checker`** — `'X'` or `'O'`

**`tiebreak`** — how the AI breaks ties when multiple columns score equally:
- `'LEFT'` — always picks the leftmost best column
- `'RIGHT'` — always picks the rightmost best column
- `'RANDOM'` — picks randomly among the best columns

**`lookahead`** — how many moves ahead the AI simulates:
- `0` — no lookahead, scores all open columns as neutral (50)
- `1` — looks one move ahead (blocks immediate wins)
- `3–4` — plays a strong game, noticeable thinking time
- `6+` — very strong but slow — each extra level multiplies computation

---

## How the AI Works

The AI uses a **minimax scoring** approach. For each available column it:

1. Simulates placing its checker there
2. Recursively asks: *"what's the best my opponent can do from here?"*
3. Scores the column based on the outcome:
   - `100` — this move leads to a win
   - `0` — this move leads to the opponent winning
   - `50` — outcome is neutral / unknown within lookahead depth
4. Picks the column with the highest score, using the tiebreak strategy for draws

---

## Example Board

```
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | |X| | | | |
|O|X|O|X| | | |
---------------
 0 1 2 3 4 5 6
```

---

## Requirements

- Python 3.x
- No external libraries required

---
