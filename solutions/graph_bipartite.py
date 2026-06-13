from collections import deque
from typing import Dict, List


def is_bipartite(graph: Dict[int, List[int]], num_nodes: int) -> bool:
    """
    Return True if the graph's nodes can be 2-colored so no edge joins same-color
    nodes (i.e. it contains no odd-length cycle).

    BFS coloring each component; a neighbour that already shares the current
    node's color breaks bipartiteness.

    Time:  O(V + E).  Space: O(V).
    """
    color = [-1] * num_nodes
    for start in range(num_nodes):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nbr in graph.get(node, []):
                if color[nbr] == -1:
                    color[nbr] = color[node] ^ 1
                    queue.append(nbr)
                elif color[nbr] == color[node]:
                    return False
    return True
