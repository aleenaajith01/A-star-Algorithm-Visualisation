# A*-Algorithm-Visualisatioon
The A* search algorithm is a popular pathfinding algorithm used in many applications, including video games, robotics, and route planning. A* is an extension of Dijkstra’s algorithm and uses heuristics to improve the efficiency of the search by prioritizing paths that are likely to be closer to the goal.

#### Step-by-step algorithm:

1. Initialize the priority queue with the start node and its heuristic value.
2. Loop until the priority queue is empty or the goal node is found:
    Pop the node with the minimum f-value (f = g + h) from the priority queue.
    If the popped node is the goal node, stop the search.
    Otherwise, expand the node and update the priority queue with the neighboring nodes and their f-values.
3. If the goal node is found, reconstruct the path.
![image](https://github.com/user-attachments/assets/0c35d898-24a6-49ed-95bf-11ea9b947c62)
