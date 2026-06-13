from typing import Tuple


def swap_numbers(a: int, b: int) -> Tuple[int, int]:
    """
    Return (a, b) with values swapped, without a temporary variable.

    Tuple packing/unpacking is the idiomatic, overflow-safe Python way
    (arithmetic/XOR tricks exist but are pointless here and risk edge bugs).

    Time:  O(1).  Space: O(1).
    """
    a, b = b, a
    return a, b
