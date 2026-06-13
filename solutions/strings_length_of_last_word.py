def length_of_last_word(s: str) -> int:
    """
    Return the length of the last word, where words are space-delimited.
    Trailing spaces are ignored.

    Scan from the right: skip trailing spaces, then count the run of
    non-spaces. Avoids allocating a split() list.

    Time:  O(n).  Space: O(1).
    """
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    length = 0
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length
