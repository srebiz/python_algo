from typing import List, Tuple


def first_circular_tour(pumps: List[Tuple[int, int]]) -> int:
    """
    Each pump gives (petrol, distance_to_next). Find the starting pump index from
    which a vehicle can complete the full circular tour, or -1 if none exists.
    (Listed under Trees in the source, but this is the classic gas-station
    greedy problem.)

    Greedy single pass: track total balance and a running tank. If the tank ever
    goes negative, no start up to here works, so reset the candidate to the next
    pump. Feasible overall iff total petrol >= total distance.

    Time:  O(n).  Space: O(1).
    """
    total = 0
    tank = 0
    start = 0
    for i, (petrol, distance) in enumerate(pumps):
        diff = petrol - distance
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 and start < len(pumps) else -1
