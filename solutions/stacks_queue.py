from typing import Optional


class Queue:
    """
    FIFO queue implemented with two stacks so each operation is amortized O(1).
    Pushes land on `_in`; pops drain `_in` into `_out` once, then pop from `_out`.

    Space: O(n).
    """

    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def enqueue(self, x: int) -> None:
        self._in.append(x)

    def dequeue(self) -> Optional[int]:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out.pop() if self._out else None

    def is_empty(self) -> bool:
        return not self._in and not self._out

    def __len__(self) -> int:
        return len(self._in) + len(self._out)
