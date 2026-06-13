def is_happy(n: int) -> bool:
    """
    A number is "happy" if repeatedly replacing it with the sum of the squares
    of its digits eventually reaches 1; otherwise it loops forever.

    Floyd cycle detection (slow/fast) avoids storing a seen-set.

    Time:  O(log n) per step, bounded total steps.  Space: O(1).
    """
    def squared_digit_sum(x: int) -> int:
        total = 0
        while x:
            x, d = divmod(x, 10)
            total += d * d
        return total

    slow, fast = n, squared_digit_sum(n)
    while fast != 1 and slow != fast:
        slow = squared_digit_sum(slow)
        fast = squared_digit_sum(squared_digit_sum(fast))
    return fast == 1
