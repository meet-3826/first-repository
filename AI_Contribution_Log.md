
### AI_Contribution_Log.md

```markdown
# AI Contribution Log – SLE-2

## Student Details
- Name: Meet Shah
- PRN: 25UAM129
- Course: 02AML204 – Introduction to Artificial Intelligence

## AI Tool Used
ChatGPT

## Contribution Details

| Activity | AI Contribution | My Contribution |
|---|---|---|
| Understanding SLE-2 | Helped explain the SLE-2 guideline and profiling requirements. | Read the faculty guideline and selected the experiment. |
| Algorithm Selection | Suggested comparing BFS and A* on the 8-puzzle. | Selected the 8-puzzle as the problem for profiling. |
| Code Structure | Helped prepare the BFS, A*, Manhattan Distance, and state-generation logic. | Created `SLE_2.py` in VS Code and ran the code. |
| Puzzle Selection | Suggested using a harder solvable 8-puzzle so profiling results would be visible. | Ran the harder puzzle and verified the results. |
| py-spy Setup | Explained installation and commands for using `py-spy`. | Installed `py-spy` and executed the profiling commands. |
| Flame Graphs | Explained how to generate separate flame graphs for BFS and A*. | Generated `bfs_profile.svg` and `astar_profile.svg`. |
| Timing | Suggested using `time.perf_counter()` and running each algorithm three times. | Ran BFS and A* three times and recorded the timings. |
| Result Analysis | Helped explain the difference between BFS and A* based on time, states explored, and heuristic use. | Checked the outputs and compared the measured results. |
| Documentation | Helped organize the report, README, and AI contribution log. | Reviewed the final content and prepared the files for submission. |

## Final Results

### BFS
- Run 1: 313.9576 ms
- Run 2: 311.8082 ms
- Run 3: 317.3513 ms
- Average: 314.3724 ms
- States Explored: 181,439
- Solution Depth: 31

### A*
- Run 1: 137.5249 ms
- Run 2: 131.1343 ms
- Run 3: 125.4256 ms
- Average: 131.3616 ms
- States Explored: 21,198
- Solution Depth: 31

## My Learning
I learned how BFS and A* behave differently on the same 8-puzzle problem. I also learned how a heuristic helps A* reduce unnecessary search, how to profile Python code using `py-spy`, and how to compare algorithms using execution time and states explored.

## Declaration
AI was used only as a support tool for understanding, code structuring, troubleshooting, and documentation. The program execution, py-spy profiling, timing runs, and collection of results were performed by me.
