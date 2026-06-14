from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(m):
    start = (m.rows, m.cols)

    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0

    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1))

    open_set = PriorityQueue()
    open_set.put((f_score[start], h(start, (1, 1)), start))

    aPath = {}
    visited = []

    while not open_set.empty():
        current_Cell = open_set.get()[2]
        visited.append(current_Cell)

        if current_Cell == (1, 1):
            break

        for d in 'ESNW':
            if m.maze_map[current_Cell][d]:

                if d == 'E':
                    child_cell = (current_Cell[0], current_Cell[1] + 1)
                elif d == 'W':
                    child_cell = (current_Cell[0], current_Cell[1] - 1)
                elif d == 'N':
                    child_cell = (current_Cell[0] - 1, current_Cell[1])
                elif d == 'S':
                    child_cell = (current_Cell[0] + 1, current_Cell[1])

                new_g_score = g_score[current_Cell] + 1
                new_f_score = new_g_score + h(child_cell, (1, 1))

                if new_f_score < f_score[child_cell]:
                    g_score[child_cell] = new_g_score
                    f_score[child_cell] = new_f_score

                    open_set.put((new_f_score, h(child_cell, (1, 1)), child_cell))

                    aPath[child_cell] = current_Cell

    if (1, 1) not in aPath:
        return None, visited

    fPath = {}
    cell = (1, 1)

    while cell != start:
        fPath[aPath[cell]] = cell
        cell = aPath[cell]

    return fPath, visited


if __name__ == '__main__':
    m = maze(5, 5)
    m.CreateMaze()

    path, visited = aStar(m)

    if path is None:
        print("No path found!")
    else:
        explored_agent = agent(m, color='red', footprints=True)
        shortest_path_agent = agent(m, color='yellow', footprints=True)
        goal_agent = agent(m, color='cyan', shape='square', filled=True)

        m.tracePath({explored_agent: visited}, delay=50)
        m.tracePath({shortest_path_agent: path})
        m.tracePath({goal_agent: [(1, 1)]})

        textLabel(m, 'A* Path Length', len(path) + 1)
        textLabel(m, ' Red', 'Explored Nodes')
        textLabel(m, ' Yellow', 'Shortest Path')
        textLabel(m, ' Cyan', 'Goal Node')

        m.run()