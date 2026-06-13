from collections import Counter
from typing import Optional


def first_non_repeating_char(s: str) -> Optional[str]:
    """
    Return the first character that appears exactly once, or None.

    One pass to count, a second pass (in original order) to find the first
    unit-count character. dict preserves insertion order in CPython 3.7+,
    so a single Counter pass keeps order intact.

    Time:  O(n).
    Space: O(k) — k = number of distinct characters.
    """
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None
