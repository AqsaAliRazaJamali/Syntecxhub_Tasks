#  Maze Solver using A* Search

A high-performance Python implementation of the **A\* Search Algorithm** designed to solve complex grid mazes. Developed as **Project 1** during my Artificial Intelligence Internship at **[Syntecxhub](https://syntecxhub.com)**.

---

## 📌 Project Overview

This module focuses on modeling a physical maze structure as an interconnected graph network of coordinate nodes. Using an intelligent state-space expansion loop guided by a **Manhattan Distance heuristic**, an autonomous agent calculates the absolute shortest path while navigating blocking barrier constraints.

The entire pathfinding workflow is visualized dynamically via a high-refresh user interface.

---

##  Core Features

-  **Procedural Generation:** Leverages `pyamaze` to generate a unique maze matrix layout on every execution.
-  **Heuristic Search:** Implements full A\* traversal optimization based on the evaluation formula $f(n) = g(n) + h(n)$.
-  **Exploration Trace (Red Agent):** Animates every coordinate evaluated within the open set queue.
-  **Optimal Solution (Yellow Agent):** Traces out the exact, mathematically shortest route from start to finish.
-  **Target Lock (Cyan Agent):** Visually locks down the target goal vector at point `(1, 1)`.
-  **Edge-Case Safety:** Robustly intercepts unreachable goal conditions without hanging or raising exceptions.
-  **Live Metrics:** Renders a clean Tkinter text label logging final trajectory costs.

---

##  Tech Stack & Architecture

| Technology / Module | Structural Role |
| :--- | :--- |
| **Python 3** | Core development runtime engine |
| **`pyamaze`** | Tkinter-wrapped graphic display layer and maze generator |
| **`queue.PriorityQueue`** | Min-Heap data array used to track the open state list |

---

## 📂 Module Context

This project sits within a central, global internship workspace structured as follows:

```text
Syntecxhub_Tasks/                     <-- Master Repository
│
└── 📁 Syntecxhub_Task1_AStar_Maze/   <-- Current Project Directory
    ├── 📄 Maze_solver.py              # Main A* engine implementation
    ├── 📄 requirements.txt            # Local Python packaging requirements
    ├── 📄 .gitignore                  # Local bytecode tracking rules
    └── 📄 README.md                   # Project documentation 
```

---

##  Installation & Local Setup

1. **Clone the master workspace:**
   ```bash
   git clone https://github.com/AqsaAliRazaJamali/Syntecxhub_Tasks.git
   cd Syntecxhub_Tasks
   ```

2. **Move inside the Task 1 subdirectory:**
   ```bash
   cd Syntecxhub_AStar_Maze
   ```

3. **Instantiate requirement packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Fire up the solver script:**
   ```bash
   python Maze_solver.py
   ```

---

##  Algorithmic Execution Model

| Component | Data Structure / Mapping | Operational Definition |
| :--- | :--- | :--- |
| **Start Node** | Coordinate Tuple `(m.rows, m.cols)` | The absolute bottom-right corner of the maze. |
| **Goal Node** | Coordinate Tuple `(1, 1)` | The target escape coordinate in the top-left corner. |
| **$g(n)$ Score** | Python Dictionary mapping | The exact traversal cost tracked from the start node to current cell $n$. |
| **$h(n)$ Heuristic** | Manhattan Distance Calculation | An admissible, consistent forecast cost minimizing path distance to target. |
| **$f(n)$ Score** | Priority total tracking | Total evaluation index ($g(n) + h(n)$) dictating node priority in queue. |

---

## ⚡ Optimized Tuple Tie-Breaking

To counter execution slowdowns when multiple alternative routes calculate identical $f(n)$ costs, nodes are enqueued using a specialized three-element tuple format:

```python
open_set.put((new_f_score, h(child_cell, (1, 1)), child_cell))
```

If an $f(n)$ collision occurs, Python's min-heap automatically defaults to the second parameter ($h$). This forces the tracking pointer to prefer nodes physically closest to the terminal point, preventing wasteful horizontal backtracking.

---

##  Heuristic Implementation

Because the agent is structurally confined to orthogonal directions (North, South, East, West) with no diagonal stepping allowed, the Manhattan Distance function is implemented:

$$h(\text{cell}) = |x_1 - x_2| + |y_1 - y_2|$$

```python
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)
```

---

##  Exception & Boundary Defenses

**Unreachable Goal Check:** If custom maze blockades close off all access routes to coordinate `(1, 1)`, the logic gracefully breaks loop execution:

```python
if (1, 1) not in aPath:
    return None, visited
```

The app avoids stack explosions, stops the UI runtime, and flushes a clean terminal warning:

```
No path found!
```

---

## 👩‍💻 Author

**Aqsa Jamali**
AI Intern @ Syntecxhub
[GitHub](https://github.com/AqsaAliRazaJamali)

---

## 📄 License

This project is developed for educational purposes as part of the Syntecxhub AI Internship Program.
