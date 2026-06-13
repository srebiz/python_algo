def is_palindrome(s: str) -> bool:
    """
    Check whether a string is a palindrome, considering only alphanumeric
    characters and ignoring case.

    Two-pointer walk from both ends inward, skipping non-alphanumerics.

    Time:  O(n) — each character inspected at most once.
    Space: O(1) — pointers only, no extra copy.
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
