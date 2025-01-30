"""
Finds the shortest path from a start node to a target node in a weighted graph using Dijkstra's algorithm.

Parameters:
- graph (dict): A dictionary representing the graph, where keys are nodes and values are lists of tuples (neighbor, weight).
- start (str): The starting node for the pathfinding.
- target (str, optional): The target node. If not provided, the function calculates paths to all nodes.

Returns:
- distances (dict): A dictionary with the shortest distance from the start node to each node.
- paths (dict): A dictionary with the shortest path from the start node to each node.

Algorithm:
1. Initialize distances to all nodes as infinity, except the start node (distance 0).
2. Use a priority queue (implicitly via `min`) to visit the node with the smallest distance.
3. Update distances and paths for neighboring nodes if a shorter path is found.
4. Repeat until all nodes are visited.

Example:
    my_graph = {
        "A": [("B", 5), ("C", 3), ("E", 11)],
        "B": [("A", 5), ("C", 1), ("F", 2)],
        "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
        "D": [("C", 1), ("E", 9), ("F", 3)],
        "E": [("A", 11), ("C", 5), ("D", 9)],
        "F": [("B", 2), ("D", 3)],
    }
    shortest_path(my_graph, "A", "F")
    # Output:
    # A-F distance: 8
    # Path: A -> C -> B -> F
"""


def shortest_path(graph, start, target=""):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )

    return distances, paths


my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


shortest_path(my_graph, "A", "F")
