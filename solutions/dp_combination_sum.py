from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    All unique combinations of candidates (each reusable unlimited times) that
    sum to target.

    Backtracking; pass a start index so combinations are non-decreasing, which
    prevents permutation duplicates.

    Time:  exponential in the worst case.  Space: O(target / min_candidate) depth.
    """
    candidates.sort()
    out: List[List[int]] = []

    def backtrack(start: int, remaining: int, path: List[int]) -> None:
        if remaining == 0:
            out.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)  # i, not i+1: reuse
            path.pop()

    backtrack(0, target, [])
    return out
