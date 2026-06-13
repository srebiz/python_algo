from typing import List


def find_celebrity(knows: List[List[int]], n: int) -> int:
    """
    A celebrity is known by everyone but knows no one. `knows[a][b] == 1` means
    a knows b. Return the celebrity's index, or -1 if none.

    Two phases: a single pass narrows to one candidate (if A knows B, A can't be
    the celebrity, so advance to B; else B can't be). Then verify the candidate.

    Time:  O(n).  Space: O(1).
    """
    candidate = 0
    for other in range(1, n):
        if knows[candidate][other]:
            candidate = other
    for i in range(n):
        if i != candidate and (knows[candidate][i] or not knows[i][candidate]):
            return -1
    return candidate
