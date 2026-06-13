def longest_valid_parentheses(s: str) -> int:
    """
    Length of the longest substring of well-formed parentheses.

    Stack of indices seeded with a -1 base. Push '(' indices; on ')' pop, then
    the distance to the new stack top is a valid run. If the stack empties,
    push the current index as a fresh base.

    Time:  O(n).  Space: O(n).
    """
    stack = [-1]
    best = 0
    for i, ch in enumerate(s):
        if ch == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
    return best
