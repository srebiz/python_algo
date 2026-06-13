class WordDictionary:
    """
    Add words and search them, where '.' in a query matches any single letter.

    Backed by a trie. Search recurses on '.' across all children of a node.

    add:    O(L).
    search: O(L) average; O(26^L) worst case when the query is all dots.
    Space:  O(total characters stored).
    """

    def __init__(self) -> None:
        self._children: dict[str, "WordDictionary"] = {}
        self._is_word = False

    def add_word(self, word: str) -> None:
        node = self
        for ch in word:
            node = node._children.setdefault(ch, WordDictionary())
        node._is_word = True

    def search(self, word: str) -> bool:
        def dfs(node: "WordDictionary", i: int) -> bool:
            if i == len(word):
                return node._is_word
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node._children.values())
            nxt = node._children.get(ch)
            return dfs(nxt, i + 1) if nxt else False

        return dfs(self, 0)
