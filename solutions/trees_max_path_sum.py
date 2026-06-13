from __future__ import annotations
from typing import Optional
from helpers import trees_common
#from helpers import trees_common /helpers/trees_common import TreeNode



def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Maximum sum of any path (a sequence of connected nodes; need not pass the
    root and need not reach a leaf).

    Post-order: each node returns the best *downward* gain (>= 0, since negative
    branches are dropped). At each node, a path may bend through it using both
    children — update the global best with left + node + right.

    Time:  O(n).  Space: O(h).
    """
    best = float("-inf")

    def gain(node: Optional[trees_common.TreeNode]) -> int:
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right)
        return node.val + max(left, right)

    gain(root)
    return int(best)
