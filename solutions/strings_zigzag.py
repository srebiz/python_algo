def zigzag_convert(s: str, num_rows: int) -> str:
    """
    Write s in a zigzag across num_rows rows then read row by row.
    "PAYPALISHIRING", 3 -> "PAHNAPLSIIGYIR".

    Walk the string assigning each char to a row, bouncing direction at the
    top and bottom rows.

    Time:  O(n).  Space: O(n) — row buffers.
    """
    if num_rows <= 1 or num_rows >= len(s):
        return s
    rows = [""] * num_rows
    row, step = 0, 1
    for ch in s:
        rows[row] += ch
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step
    return "".join(rows)
