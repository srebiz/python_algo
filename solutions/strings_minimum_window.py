from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Smallest substring of s containing every character of t (with multiplicity).
    Returns "" if none exists.

    Sliding window with a "need/have" satisfied-count: grow right until the
    window is valid, then shrink left while keeping it valid, tracking the best.

    Time:  O(|s| + |t|).  Space: O(|t|).
    """
    if not s or not t:
        return ""
    need = Counter(t)
    required = len(need)
    have = 0
    counts: dict[str, int] = {}
    best_len, best_start = float("inf"), 0
    left = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        if ch in need and counts[ch] == need[ch]:
            have += 1
        while have == required:
            if right - left + 1 < best_len:
                best_len, best_start = right - left + 1, left
            lch = s[left]
            counts[lch] -= 1
            if lch in need and counts[lch] < need[lch]:
                have -= 1
            left += 1
    return "" if best_len == float("inf") else s[best_start:best_start + best_len]
