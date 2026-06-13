def longest_substring_without_repeating(s: str) -> int:
    """
    Length of the longest substring containing no repeated character.
    (Covers both "Longest Substring" and "...Without Repeating Characters".)

    Sliding window: expand right; when a repeat appears, jump the left edge
    to just past the previous occurrence of that character.

    Time:  O(n).  Space: O(k) — distinct characters in the window.
    """
    last_seen: dict[str, int] = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
