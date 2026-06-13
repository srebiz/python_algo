from typing import List, Optional


class CircularQueue:
    """
    Fixed-capacity ring buffer. A head index plus a size counter avoids the
    classic "full vs empty look identical" ambiguity.

    enqueue/dequeue/peek: O(1).  Space: O(capacity).
    """

    def __init__(self, capacity: int) -> None:
        self._buf: List[Optional[int]] = [None] * capacity
        self._cap = capacity
        self._head = 0
        self._size = 0

    def enqueue(self, x: int) -> bool:
        if self._size == self._cap:
            return False
        tail = (self._head + self._size) % self._cap
        self._buf[tail] = x
        self._size += 1
        return True

    def dequeue(self) -> Optional[int]:
        if self._size == 0:
            return None
        x = self._buf[self._head]
        self._head = (self._head + 1) % self._cap
        self._size -= 1
        return x

    def peek(self) -> Optional[int]:
        return None if self._size == 0 else self._buf[self._head]

    def is_full(self) -> bool:
        return self._size == self._cap

    def is_empty(self) -> bool:
        return self._size == 0
