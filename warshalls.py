def warshall(graph):
    """
    Find the transitive closure of a graph using Warshall's algorithm.

    :param graph: A 2D list representing an adjacency matrix of a graph.
                  graph[i][j] is 1 if there is an edge between nodes i and j, and 0 otherwise.
    :return: A 2D list representing the transitive closure of the graph.
    """

    # Initialize the transitive closure matrix as a copy of the input graph
    closure = [row[:] for row in graph]

    # Iterate over all pairs of nodes (i, j) and (j, k)
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                # If there is a path from i to j through k, update the closure
                if closure[i][k] == 1 and closure[k][j] == 1:
                    closure[i][j] = 1

    return closure

# Example usage
graph = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

transitive_closure = warshall(graph)
print(transitive_closure)