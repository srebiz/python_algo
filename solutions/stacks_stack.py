from typing import List, Optional


class Stack:
    """
    LIFO stack over a Python list. push/pop/peek are amortized O(1).

    Space: O(n).
    """

    def __init__(self) -> None:
        self._items: List[int] = []

    def push(self, x: int) -> None:
        self._items.append(x)

    def pop(self) -> Optional[int]:
        return self._items.pop() if self._items else None

    def peek(self) -> Optional[int]:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)
