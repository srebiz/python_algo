from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Return the longest string that prefixes every input string.

    Vertical scan: compare characters column by column across all strings;
    stop at the first mismatch or when any string ends.

    Time:  O(S) — S = total characters across all strings.
    Space: O(1) beyond the output.
    """
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for other in strs[1:]:
            if i >= len(other) or other[i] != ch:
                return strs[0][:i]
    return strs[0]
