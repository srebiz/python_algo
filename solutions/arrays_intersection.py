from typing import List


def intersection(a: List[int], b: List[int]) -> List[int]:
    """
    Return the distinct values present in both lists.

    Hash one list into a set, then filter the other; a result set avoids
    duplicate outputs.

    Time:  O(m + n).  Space: O(min(m, n)).
    """
    set_a = set(a)
    out: List[int] = []
    emitted: set[int] = set()
    for x in b:
        if x in set_a and x not in emitted:
            emitted.add(x)
            out.append(x)
    return out
