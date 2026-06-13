from collections import Counter
from typing import Optional


def max_occurring_char(s: str) -> Optional[str]:
    """
    Return the most frequently occurring character. Ties broken by first
    appearance order. Returns None for an empty string.

    Time:  O(n).
    Space: O(k) — k = distinct characters.
    """
    if not s:
        return None
    counts = Counter(s)
    best_char, best_count = s[0], 0
    for ch in s:                       # original order => stable tie-break
        if counts[ch] > best_count:
            best_char, best_count = ch, counts[ch]
    return best_char
