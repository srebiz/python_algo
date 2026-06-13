from typing import Dict, List


def has_cycle_directed(graph: Dict[int, List[int]], num_nodes: int) -> bool:
    """
    Detect a cycle in a directed graph given as an adjacency map.

    DFS with three colors: 0 unvisited, 1 in the current recursion stack,
    2 fully done. An edge to a "1" node is a back edge => cycle.

    Time:  O(V + E).  Space: O(V).
    """
    state = [0] * num_nodes

    def dfs(node: int) -> bool:
        state[node] = 1
        for nbr in graph.get(node, []):
            if state[nbr] == 1:
                return True
            if state[nbr] == 0 and dfs(nbr):
                return True
        state[node] = 2
        return False

    return any(state[n] == 0 and dfs(n) for n in range(num_nodes))
