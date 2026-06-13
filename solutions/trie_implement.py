class Trie:
    """
    Prefix tree supporting insert, exact-word search, and prefix search.

    Each node holds a dict of child characters and an end-of-word flag.

    insert / search / starts_with: O(L) — L = key length.
    Space: O(total characters inserted).
    """

    def __init__(self) -> None:
        self._children: dict[str, "Trie"] = {}
        self._is_word = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            node = node._children.setdefault(ch, Trie())
        node._is_word = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node._is_word

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s: str) -> "Trie | None":
        node = self
        for ch in s:
            nxt = node._children.get(ch)
            if nxt is None:
                return None
            node = nxt
        return node
