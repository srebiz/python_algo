def is_valid_parentheses(s: str) -> bool:
    """
    Return True if every bracket is correctly opened and closed in order.

    Push openers onto a stack; on a closer, the stack top must be its match.

    Time:  O(n).  Space: O(n) — worst case all openers.
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
