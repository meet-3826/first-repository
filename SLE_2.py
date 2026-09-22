from collections import deque
import time
import heapq
import sys

START_STATE = (
    8, 6, 7,
    2, 5, 4,
    3, 0, 1
)

GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


def get_neighbors(state):
    neighbors = []

    blank_position = state.index(0)
    row = blank_position // 3
    col = blank_position % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for row_change, col_change in moves:
        new_row = row + row_change
        new_col = col + col_change

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_position = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank_position], new_state[new_position] = (
                new_state[new_position],
                new_state[blank_position]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def bfs(start, goal):
    queue = deque()
    queue.append((start, 0))

    visited = {start}
    states_explored = 0

    while queue:
        current_state, depth = queue.popleft()
        states_explored += 1

        if current_state == goal:
            return depth, states_explored

        for next_state in get_neighbors(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, depth + 1))

    return -1, states_explored


def manhattan_distance(state):
    total_distance = 0

    for value in range(1, 9):
        current_position = state.index(value)
        goal_position = GOAL_STATE.index(value)

        current_row = current_position // 3
        current_col = current_position % 3

        goal_row = goal_position // 3
        goal_col = goal_position % 3

        total_distance += abs(current_row - goal_row)
        total_distance += abs(current_col - goal_col)

    return total_distance


def astar(start, goal):
    priority_queue = []

    heapq.heappush(
        priority_queue,
        (manhattan_distance(start), 0, start)
    )

    best_cost = {start: 0}
    states_explored = 0

    while priority_queue:
        f_cost, g_cost, current_state = heapq.heappop(priority_queue)

        states_explored += 1

        if current_state == goal:
            return g_cost, states_explored

        for next_state in get_neighbors(current_state):
            new_cost = g_cost + 1

            if next_state not in best_cost or new_cost < best_cost[next_state]:
                best_cost[next_state] = new_cost

                heuristic = manhattan_distance(next_state)

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost + heuristic,
                        new_cost,
                        next_state
                    )
                )

    return -1, states_explored


def run_bfs():
    print("8-Puzzle using BFS")

    start_time = time.perf_counter()

    depth, explored = bfs(START_STATE, GOAL_STATE)

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000

    print("Solution Depth:", depth)
    print("States Explored:", explored)
    print("Execution Time:", round(execution_time, 4), "ms")


def run_astar():
    print("8-Puzzle using A*")

    start_time = time.perf_counter()

    depth, explored = astar(START_STATE, GOAL_STATE)

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000

    print("Solution Depth:", depth)
    print("States Explored:", explored)
    print("Execution Time:", round(execution_time, 4), "ms")

def main():
    if len(sys.argv) < 2:
        print("Please choose an algorithm.")
        print("Use:")
        print("python puzzle_8.py bfs")
        print("or")
        print("python puzzle_8.py astar")
        return

    algorithm = sys.argv[1].lower()

    if algorithm == "bfs":
        run_bfs()

    elif algorithm == "astar":
        run_astar()

    else:
        print("Invalid algorithm.")
        print("Please use 'bfs' or 'astar'.")


if __name__ == "__main__":
    main()