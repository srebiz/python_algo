def is_isomorphic(s: str, t: str) -> bool:
    """
    Return True if characters in s can be mapped one-to-one onto characters
    in t preserving order (a bijection). 'egg'/'add' -> True, 'foo'/'bar' -> False.

    Track two maps (s->t and t->s); a conflict in either breaks the bijection.

    Time:  O(n).  Space: O(k) — distinct characters.
    """
    if len(s) != len(t):
        return False
    forward: dict[str, str] = {}
    backward: dict[str, str] = {}
    for cs, ct in zip(s, t):
        if forward.setdefault(cs, ct) != ct:
            return False
        if backward.setdefault(ct, cs) != cs:
            return False
    return True
