def count_ways_to_cover_distance(distance: int) -> int:
    """
    Number of ways to cover `distance` taking steps of 1, 2, or 3 at a time.

    Tribonacci recurrence: ways(d) = ways(d-1) + ways(d-2) + ways(d-3), rolled
    forward with three variables.

    Time:  O(distance).  Space: O(1).
    """
    if distance < 0:
        return 0
    a, b, c = 1, 0, 0          # ways for distance -2, -1, 0 conceptually
    # seed so that the first computed value corresponds to distance 1
    w0, w1, w2 = 1, 1, 2        # ways(0), ways(1), ways(2)
    if distance == 0:
        return w0
    if distance == 1:
        return w1
    if distance == 2:
        return w2
    for _ in range(3, distance + 1):
        w0, w1, w2 = w1, w2, w0 + w1 + w2
    return w2
