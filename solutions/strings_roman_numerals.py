def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral to an integer.

    Scan left to right; if a symbol is smaller than the one to its right it is
    subtractive (e.g. IV = 4), so subtract it, otherwise add it.

    Time:  O(n).  Space: O(1).
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
            total -= values[ch]
        else:
            total += values[ch]
    return total


def int_to_roman(num: int) -> str:
    """
    Convert an integer (1..3999) to a Roman numeral via greedy subtraction
    over value/symbol pairs ordered high to low.

    Time:  O(1) — fixed-size table.  Space: O(1).
    """
    table = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
             (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = []
    for value, symbol in table:
        count, num = divmod(num, value)
        out.append(symbol * count)
    return "".join(out)
