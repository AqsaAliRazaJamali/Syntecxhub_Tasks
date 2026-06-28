# Syntecxhub Internship - Artificial Intelligence (AI)

Welcome to my central repository documenting my progress during the **Syntecxhub Artificial Intelligence Internship**. This repository acts as a comprehensive dashboard showcasing algorithmic implementations, machine learning models, and automated AI solutions completed throughout the program.

---

##  Internship Roadmap & Status

| Phase / Task | Project Module | Technical Core | Status |
| :--- | :--- | :--- | :--- |
| **Task 1** | 🚀 [Maze Solver using A* Search](./Syntecxhub_AStar_Maze) | Heuristic Search, State Space Graphs, Manhattan Distance | `🟢Completed` |
| **Task 2** | 🚀 [Sentiment Analysis Tool](./Syntecxhub_Sentiment_Analysis_Tool) | Natural Language Processing (NLP), Text Vectorization, Supervised Classifiers | `🟢Completed` |
| **Task 3** | 🔹 Upcoming AI Task | *To be determined* | `⏳ Pending` |

---

##  Project Deep-Dives

### Task 1:  Maze Solver via A* Search
- **Objective:** Model a dynamic grid environment as an interconnected graph network of state nodes and discover the absolute shortest path while ignoring blocking barriers.
- **AI Core:** Evaluates neighboring nodes mathematically using the evaluation function:
  $$f(n) = g(n) + h(n)$$
  Where $g(n)$ is the exact cost from the start node to the current cell, and $h(n)$ is the estimated cost to the goal using **Manhattan Distance** heuristics. Includes customized tie-breaking tuple logic to keep the search beam focused directly toward the target destination.
- **UI Component:** Uses an interactive, high-refresh Tkinter visualizer (`pyamaze`) to trace agent footprint expansion in real-time.

### Task 2: Sentiment Analysis Tool
- **Objective:** Build an end-to-end classification pipeline to load text arrays, run text sanitation patterns, transform descriptive strings into geometric numeric vectors, and train predictive weights.
- **AI Core:** Integrates text vectorization transforms (TF-IDF / Count Matrix) alongside probabilistic structural models (**Multinomial Naive Bayes**) and linear classification layers (**Logistic Regression** with balanced class weighting variables).
- **UI Component:** Launches a direct interactive text analysis shell checking customized test inputs, displaying real-time confidence scores and localized probability parameters.

---

##  Global Environment Setup

To clone this repository and explore individual AI modules locally, use the following execution workflow in your terminal:

```bash
# 1. Clone the master repository
git clone [https://github.com/AqsaAliRazaJamali/Syntecxhub_Tasks.git](https://github.com/AqsaAliRazaJamali/Syntecxhub_Tasks.git)

# 2. Navigate into the root path
cd Syntecxhub_Tasks

# 3. Enter the specific AI task directory (e.g., Task 1)
cd Syntecxhub_AStar_Maze

# 4. Install localized package dependencies
pip install -r requirements.txt

# 5. Launch the AI engine
python Maze_solver.py

---

## 👩‍💻 Author

<div align="center">

### **Aqsa Jamali**

**AI Intern @ Syntecxhub**

Passionate about **Artificial Intelligence, Machine Learning, and Software Engineering**.

[![GitHub](https://img.shields.io/badge/GitHub-AqsaAliRazaJamali-181717?style=for-the-badge&logo=github)](https://github.com/AqsaAliRazaJamali)

</div>

