from typing import Dict, List, Tuple


def find_bridges(graph: Dict[int, List[int]], num_nodes: int) -> List[Tuple[int, int]]:
    """
    Find all bridges (edges whose removal disconnects the graph) in an undirected
    graph using Tarjan's algorithm.

    DFS assigns discovery times; `low[u]` is the earliest reachable discovery
    time from u's subtree. Edge (u, v) is a bridge iff low[v] > disc[u].

    Time:  O(V + E).  Space: O(V).
    """
    disc = [-1] * num_nodes
    low = [0] * num_nodes
    bridges: List[Tuple[int, int]] = []
    timer = [0]

    def dfs(u: int, parent: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph.get(u, []):
            if v == parent:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    bridges.append((u, v))
            else:
                low[u] = min(low[u], disc[v])

    for node in range(num_nodes):
        if disc[node] == -1:
            dfs(node, -1)
    return bridges
