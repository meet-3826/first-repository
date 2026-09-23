# SLE-2: 8-Puzzle Profiling using BFS and A*

## Project Overview

This project compares the performance of Breadth-First Search (BFS) and A* Search on the same 8-puzzle problem.

The comparison is based on:
- Execution time
- States explored
- Solution depth
- py-spy profiling graphs

## Problem Statement

The 8-puzzle is a 3 × 3 sliding-tile puzzle. The goal is to move the tiles from the start state to the goal state.

### Start State

8 6 7
2 5 4
3 0 1

### Goal State

1 2 3
4 5 6
7 8 0

Here, 0 represents the blank tile.

## Algorithms Used

### Breadth-First Search (BFS)
BFS explores states level by level. It can find the shortest solution when all moves have equal cost, but it may explore many states.

### A* Search
A* uses a heuristic to guide the search toward the goal. In this project, Manhattan Distance is used as the heuristic.

## Profiling Method

The program was profiled using py-spy.

Execution time was measured using `time.perf_counter()`.

Each algorithm was executed 3 times and the number of states explored was also recorded.

## Results

| Metric | BFS | A* |
|---|---:|---:|
| Average Time (ms) | 314.3724 | 131.3616 |
| States Explored | 181,439 | 21,198 |
| Solution Depth | 31 | 31 |

## Observation

Both algorithms found the solution at depth 31.

A* explored fewer states and required less execution time than BFS because the Manhattan Distance heuristic guided the search toward more promising states.

## Profiling Files

- `bfs_profile.svg`
- `astar_profile.svg`

## Conclusion

This experiment helped me understand the practical difference between uninformed and informed search algorithms.

For the selected 8-puzzle problem, A* was more efficient than BFS because it explored fewer states and required less execution time.
