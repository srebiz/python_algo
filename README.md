# DEA Python Exercises

Complete solutions to the Data Engineer Academy Python exercise set. Every solution
lives in its own file under `solutions/`, with type hints, a docstring, and a
Big-O complexity note. `main.py` imports each one and runs it against a few
deliberately chosen edge-case inputs; the `assert`s in it double as lightweight
regression tests.

## Run

```bash
python main.py
```

A clean run ends with **"All demos passed (Batch 1 + Batch 2)"** — no
`AssertionError`, exit code 0 — meaning every sampled case passed. No
third-party dependencies; standard library only, Python 3.9+.

## Layout

```
python-exercises/
├── main.py                     # demo + assertion runner
├── solutions/
│   ├── __init__.py
│   ├── linkedlist_common.py    # shared ListNode + build/convert helpers
│   ├── trees_common.py         # shared TreeNode + level-order builder
│   └── <category>_<name>.py    # one exercise per file
└── README.md
```

## Notes on the source list

The original list had merged lines and a few duplicates. These were
de-duplicated as follows:

- **Longest Substring** / **Longest Substring Without Repeating Characters** → one file (`strings_longest_substring.py`).
- **Longest Common Prefix** (Easy + Hard) → one file.
- **Largest Subarray Sum** / **Max Subarray Sum** → one Kadane file (`arrays_max_subarray_sum.py`).
- **Spiral Matrix** / **Traversal of Spiral Matrix** → one file.
- **Existence of a Word** → covered by `strings_word_search.py`.
- **Validation of a Binary Tree** / **Validate Binary Search Tree** → one file (Batch 2).
- **Triplets** (DP/Greedy) was ambiguous in the source; implemented as
  **count triplets with sum strictly below a target** (`dp_triplets.py`), an O(n^2)
  sort + two-pointer approach.
- **Find the First Circular Tour that Visits All Petrol Pumps** was listed under
  Trees but is the classic gas-station greedy problem; filed as `graph_petrol_pump_tour.py`.

The trailing access status (Onboarding / To do) was ignored, as requested.

## Coverage

### Batch 1 ✅

**Strings**: Palindrome · First Non-Repeating Character · Maximum Occurring
Character · Roman Numerals (both directions) · Valid Parentheses · Length of
Last Word · Longest Common Prefix · Isomorphic Strings · Longest Substring
Without Repeating · Zigzag Pattern · Longest Palindromic Substring · Minimum
Window Substring · Word Search · Add and Search Word · Longest Valid Parentheses

**Math / Numbers**: Prime Number · Fibonacci Series · Swap Numbers · Armstrong
Number · Happy Number · The Celebrity Problem

**Lists & Arrays**: Max Element · Remove Duplicates · Reverse List · Merge
Sorted Arrays · Linear Search · Largest & Smallest · First Occurrence ·
Intersection · Max Subarray Sum (Kadane) · Binary Search · Rotate Image ·
First & Last Position · Buy/Sell Stock · Spiral Matrix · Largest Number ·
Container With Most Water · Trapping Rain Water · Chocolate Distribution ·
Search Rotated Sorted Array · Insert Interval · Merge Intervals · Set Matrix
Zeroes · Median from Data Stream · 3Sum · Top K Frequent · Largest Triplet
Product in a Stream · Two Sum · Reverse Integer · Median of Two Sorted Arrays ·
3Sum Closest · Substring with Concatenation of All Words · First Missing
Positive · Transpose of Matrix

**Linked Lists**: Singly Linked List · Circular (cycle detect) · Cycle Start
Node · Reverse · Merge K Sorted · Remove Duplicates · Find Middle · Add Two
Numbers · Max Element · Delete Last Occurrence

**Stacks & Queues**: Stack · Queue · Circular Queue · Infix→Postfix · Next
Greater Element · Delete Middle of Stack

### Batch 2 ✅

**Trees & Binary Trees**: Height · Validate BST · Traversals · Right View ·
Same Structure · Invert/Flip · Max Path Sum · Level Order · Subtree of Another
Tree · Construct from Preorder+Inorder · Kth Smallest in BST

**Trie**: Implement Trie (Prefix Tree)

**Dynamic Programming / Greedy**: Triplets (count-below-sum) · Connect N Ropes · Climb Stairs ·
Coin Change · 0/1 Knapsack · Dice Throw · Longest Increasing Subsequence · Egg
Dropping · Matrix Chain Multiplication · Combination Sum · House Robber · Decode
Ways · Unique Paths with Obstacles · Jump Game · Rod Cutting · Max Product
Cutting · Count Ways to Cover Distance

**Graph / Matrix**: Number of Islands · Snake & Ladder · Detect Cycle (Directed)
· Bridges · Bipartite Check · Largest Region · Flood Fill · Petrol Pump Tour

**Advanced**: N-ary Tree Mirror of Itself
