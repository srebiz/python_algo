def infix_to_postfix(expr: str) -> str:
    """
    Convert an infix expression to postfix (Reverse Polish) via the
    shunting-yard algorithm. Supports + - * / ^ and parentheses; tokens are
    single-character operands.

    Operators pop while the stack top has greater-or-equal precedence (strictly
    greater for right-associative '^').

    Time:  O(n).  Space: O(n).
    """
    prec = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    right_assoc = {"^"}
    out: list[str] = []
    ops: list[str] = []
    for ch in expr:
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            ops.append(ch)
        elif ch == ")":
            while ops and ops[-1] != "(":
                out.append(ops.pop())
            ops.pop()                      # discard '('
        elif ch in prec:
            while (ops and ops[-1] != "(" and
                   (prec[ops[-1]] > prec[ch] or
                    (prec[ops[-1]] == prec[ch] and ch not in right_assoc))):
                out.append(ops.pop())
            ops.append(ch)
    while ops:
        out.append(ops.pop())
    return "".join(out)
