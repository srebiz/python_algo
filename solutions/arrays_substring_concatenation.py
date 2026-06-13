from collections import Counter
from typing import List


def find_substring(s: str, words: List[str]) -> List[int]:
    """
    Start indices in s of substrings that are a concatenation of every word in
    `words` exactly once (all words share one length), in any order.

    Slide a window of total length; for each of `word_len` offsets, count words
    and validate against the required multiset.

    Time:  O(len(s) * word_len).  Space: O(len(words) * word_len).
    """
    if not s or not words:
        return []
    word_len = len(words[0])
    total = word_len * len(words)
    need = Counter(words)
    out: List[int] = []
    for offset in range(word_len):
        left = offset
        seen: Counter = Counter()
        count = 0
        for right in range(offset, len(s) - word_len + 1, word_len):
            w = s[right:right + word_len]
            if w in need:
                seen[w] += 1
                count += 1
                while seen[w] > need[w]:
                    seen[s[left:left + word_len]] -= 1
                    left += word_len
                    count -= 1
                if count == len(words):
                    out.append(left)
            else:
                seen.clear()
                count = 0
                left = right + word_len
    return out
