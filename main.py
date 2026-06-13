"""
DEA Python Exercises — demonstration runner (Batch 1).

Imports every solution and exercises it on a few deliberately chosen edge-case
inputs. Run from the project root:

    python main.py

Each block prints a result line; `assert`s double as lightweight regression
tests, so a clean run with no AssertionError means every solution behaves as
expected on the sampled cases.
"""
from builders.linkedlist_common import build_list, to_pylist
from helpers.trees_common import build_tree, TreeNode


def section(title: str) -> None:
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


# --------------------------------------------------------------------------- #
# Strings
# --------------------------------------------------------------------------- #
def demo_strings() -> None:
    section("STRINGS")

    from solutions.strings_palindrome import is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("race a car")
    assert is_palindrome("")                       # edge: empty is a palindrome
    print("palindrome:", is_palindrome("Was it a car or a cat I saw?"))

    from solutions.strings_first_non_repeating_char import first_non_repeating_char
    assert first_non_repeating_char("leetcode") == "l"
    assert first_non_repeating_char("aabb") is None   # edge: none unique
    print("first non-repeating ('swiss'):", first_non_repeating_char("swiss"))

    from solutions.strings_max_occurring_char import max_occurring_char
    assert max_occurring_char("test sample") == "t"
    assert max_occurring_char("") is None
    print("max occurring ('mississippi'):", max_occurring_char("mississippi"))

    from solutions.strings_roman_numerals import roman_to_int, int_to_roman
    assert roman_to_int("MCMXCIV") == 1994          # subtractive cases
    assert int_to_roman(1994) == "MCMXCIV"
    print("roman 3888 ->", int_to_roman(3888))

    from solutions.strings_valid_parentheses import is_valid_parentheses
    assert is_valid_parentheses("()[]{}")
    assert not is_valid_parentheses("(]")
    assert is_valid_parentheses("")                 # edge: empty is valid
    print("valid '([{}])':", is_valid_parentheses("([{}])"))

    from solutions.strings_length_of_last_word import length_of_last_word
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    assert length_of_last_word("a") == 1
    print("last word len ('Hello World'):", length_of_last_word("Hello World"))

    from solutions.strings_longest_common_prefix import longest_common_prefix
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "car"]) == ""   # edge: no common prefix
    print("LCP ['ab','abc']:", repr(longest_common_prefix(["ab", "abc"])))

    from solutions.strings_isomorphic import is_isomorphic
    assert is_isomorphic("egg", "add")
    assert not is_isomorphic("foo", "bar")
    assert not is_isomorphic("badc", "baba")        # edge: breaks bijection
    print("isomorphic 'paper'/'title':", is_isomorphic("paper", "title"))

    from solutions.strings_longest_substring import longest_substring_without_repeating
    assert longest_substring_without_repeating("abcabcbb") == 3
    assert longest_substring_without_repeating("") == 0
    assert longest_substring_without_repeating("bbbbb") == 1
    print("longest substring 'pwwkew':",
          longest_substring_without_repeating("pwwkew"))

    from solutions.strings_zigzag import zigzag_convert
    assert zigzag_convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert zigzag_convert("ABC", 1) == "ABC"        # edge: single row
    print("zigzag 4 rows:", zigzag_convert("PAYPALISHIRING", 4))

    from solutions.strings_longest_palindromic_substring import longest_palindromic_substring
    assert longest_palindromic_substring("babad") in {"bab", "aba"}
    assert longest_palindromic_substring("cbbd") == "bb"
    print("longest palindrome 'forgeeksskeegfor':",
          longest_palindromic_substring("forgeeksskeegfor"))

    from solutions.strings_minimum_window import min_window
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "aa") == ""              # edge: impossible
    print("min window:", min_window("ADOBECODEBANC", "ABC"))

    from solutions.strings_word_search import word_search
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert word_search([row[:] for row in board], "ABCCED")
    assert not word_search([row[:] for row in board], "ABCB")  # edge: reuse banned
    print("word search 'SEE':", word_search([row[:] for row in board], "SEE"))

    from solutions.strings_add_and_search_word import WordDictionary
    wd = WordDictionary()
    for w in ("bad", "dad", "mad"):
        wd.add_word(w)
    assert not wd.search("pad")
    assert wd.search("bad")
    assert wd.search(".ad")                         # wildcard
    assert wd.search("b..")
    print("add/search 'b..':", wd.search("b.."))

    from solutions.strings_longest_valid_parentheses import longest_valid_parentheses
    assert longest_valid_parentheses(")()())") == 4
    assert longest_valid_parentheses("") == 0
    print("longest valid '(()':", longest_valid_parentheses("(()"))


# --------------------------------------------------------------------------- #
# Math / Numbers
# --------------------------------------------------------------------------- #
def demo_math() -> None:
    section("MATH / NUMBERS")

    from solutions.math_prime_number import is_prime
    assert is_prime(2) and is_prime(97)
    assert not is_prime(1) and not is_prime(0) and not is_prime(-7)  # edges
    print("is_prime(7919):", is_prime(7919))

    from solutions.math_fibonacci import fibonacci_series
    assert fibonacci_series(0) == []
    assert fibonacci_series(1) == [0]
    assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
    print("fib(10):", fibonacci_series(10))

    from solutions.math_swap_numbers import swap_numbers
    assert swap_numbers(3, 9) == (9, 3)
    assert swap_numbers(-1, -1) == (-1, -1)
    print("swap(5, 7):", swap_numbers(5, 7))

    from solutions.math_armstrong import is_armstrong
    assert is_armstrong(153) and is_armstrong(9474)
    assert is_armstrong(0)
    assert not is_armstrong(100)
    print("is_armstrong(371):", is_armstrong(371))

    from solutions.math_happy_number import is_happy
    assert is_happy(19) and is_happy(1)
    assert not is_happy(2)                          # edge: known unhappy loop
    print("is_happy(7):", is_happy(7))

    from solutions.math_celebrity import find_celebrity
    # 2 is known by all and knows no one.
    knows = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    assert find_celebrity(knows, 3) == 2
    no_celeb = [[0, 1], [1, 0]]
    assert find_celebrity(no_celeb, 2) == -1        # edge: none
    print("celebrity:", find_celebrity(knows, 3))


# --------------------------------------------------------------------------- #
# Lists & Arrays
# --------------------------------------------------------------------------- #
def demo_arrays() -> None:
    section("LISTS & ARRAYS")

    from solutions.arrays_max_element import max_element
    assert max_element([3, 7, 2, 7]) == 7
    assert max_element([]) is None                  # edge: empty
    assert max_element([-5]) == -5
    print("max_element:", max_element([1, 9, 4]))

    from solutions.arrays_remove_duplicates import remove_duplicates
    assert remove_duplicates([1, 1, 2, 3, 3, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []
    print("remove_duplicates:", remove_duplicates([4, 4, 5, 4, 6]))

    from solutions.arrays_reverse_list import reverse_list
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([1]) == [1]
    print("reverse_list:", reverse_list([1, 2, 3, 4]))

    from solutions.arrays_merge_sorted import merge_sorted
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([], [1, 2]) == [1, 2]       # edge: one empty
    print("merge_sorted:", merge_sorted([1, 4], [2, 3, 5]))

    from solutions.arrays_linear_search import linear_search
    assert linear_search([5, 3, 8], 8) == 2
    assert linear_search([5, 3, 8], 9) == -1        # edge: absent
    print("linear_search:", linear_search([1, 2, 3], 2))

    from solutions.arrays_largest_smallest import largest_and_smallest
    assert largest_and_smallest([3, 1, 9, 4]) == (9, 1)
    assert largest_and_smallest([]) is None
    print("largest_and_smallest:", largest_and_smallest([7]))

    from solutions.arrays_first_occurrence import first_occurrence
    assert first_occurrence([2, 4, 4, 6], 4) == 1
    assert first_occurrence([1], 9) == -1
    print("first_occurrence:", first_occurrence([5, 5, 5], 5))

    from solutions.arrays_intersection import intersection
    assert sorted(intersection([1, 2, 2, 3], [2, 3, 4])) == [2, 3]
    assert intersection([1], [2]) == []             # edge: disjoint
    print("intersection:", intersection([1, 2, 3], [3, 2, 9]))

    from solutions.arrays_max_subarray_sum import max_subarray_sum
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray_sum([-3, -1, -2]) == -1     # edge: all negative
    print("max_subarray_sum:", max_subarray_sum([5, -2, 3]))

    from solutions.arrays_binary_search import binary_search
    assert binary_search([1, 3, 5, 7, 9], 7) == 3
    assert binary_search([1, 3, 5], 4) == -1        # edge: absent
    assert binary_search([], 1) == -1
    print("binary_search:", binary_search([2, 4, 6, 8], 8))

    from solutions.arrays_rotate_image import rotate_image
    assert rotate_image([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    print("rotate_image:", rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    from solutions.arrays_first_last_position import first_last_position
    assert first_last_position([5, 7, 7, 8, 8, 10], 8) == (3, 4)
    assert first_last_position([5, 7, 7, 8, 8, 10], 6) == (-1, -1)  # edge: gap
    print("first_last_position:", first_last_position([2, 2], 2))

    from solutions.arrays_buy_sell_stock import max_profit
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0         # edge: only losses
    print("max_profit:", max_profit([2, 4, 1]))

    from solutions.arrays_spiral_matrix import spiral_order
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([]) == []                   # edge: empty
    print("spiral_order:", spiral_order([[1, 2], [3, 4]]))

    from solutions.arrays_largest_number import largest_number
    assert largest_number([3, 30, 34, 5, 9]) == "9534330"
    assert largest_number([0, 0]) == "0"            # edge: all zeros
    print("largest_number:", largest_number([10, 2]))

    from solutions.arrays_container_most_water import max_area
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    print("max_area:", max_area([4, 3, 2, 1, 4]))

    from solutions.arrays_trapping_rain_water import trap
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([]) == 0                            # edge: empty
    print("trap:", trap([4, 2, 0, 3, 2, 5]))

    from solutions.arrays_chocolate_distribution import min_chocolate_diff
    assert min_chocolate_diff([7, 3, 2, 4, 9, 12, 56], 3) == 2
    print("min_chocolate_diff:", min_chocolate_diff([3, 4, 1, 9, 56, 7, 9, 12], 5))

    from solutions.arrays_search_rotated_sorted import search_rotated
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1   # edge: absent
    print("search_rotated:", search_rotated([1], 1))

    from solutions.arrays_insert_interval import insert_interval
    assert insert_interval([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert_interval([], [4, 8]) == [[4, 8]]  # edge: empty list
    print("insert_interval:",
          insert_interval([[1, 2], [3, 5], [6, 7], [8, 10]], [4, 9]))

    from solutions.arrays_merge_intervals import merge_intervals
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]   # edge: touching
    print("merge_intervals:", merge_intervals([[1, 4], [2, 3]]))

    from solutions.arrays_set_matrix_zeroes import set_matrix_zeroes
    assert set_matrix_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == \
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    print("set_matrix_zeroes:", set_matrix_zeroes([[0, 1], [1, 1]]))

    from solutions.arrays_median_data_stream import MedianFinder
    mf = MedianFinder()
    mf.add_num(1); mf.add_num(2)
    assert mf.find_median() == 1.5                  # even count -> average
    mf.add_num(3)
    assert mf.find_median() == 2.0                  # odd count -> middle
    print("median stream:", mf.find_median())

    from solutions.arrays_3sum import three_sum
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]      # edge: all zeros
    print("three_sum:", three_sum([-2, 0, 1, 1, 2]))

    from solutions.arrays_top_k_frequent import top_k_frequent
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([5], 1) == [5]
    print("top_k_frequent:", top_k_frequent([4, 4, 4, 6, 6, 7], 2))

    from solutions.arrays_largest_triplet_product import largest_triplet_products
    assert largest_triplet_products([1, 2, 3, 4, 5]) == [None, None, 6, 24, 60]
    print("largest_triplet_products:", largest_triplet_products([10, 3, 5, 6, 20]))

    from solutions.arrays_two_sum import two_sum
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum([1, 2], 10) is None              # edge: no pair
    print("two_sum:", two_sum([3, 2, 4], 6))

    from solutions.arrays_reverse_integer import reverse_integer
    assert reverse_integer(-123) == -321
    assert reverse_integer(120) == 21               # edge: trailing zero
    assert reverse_integer(1534236469) == 0         # edge: 32-bit overflow
    print("reverse_integer:", reverse_integer(123))

    from solutions.arrays_median_two_sorted import median_two_sorted
    assert median_two_sorted([1, 3], [2]) == 2.0
    assert median_two_sorted([1, 2], [3, 4]) == 2.5
    print("median_two_sorted:", median_two_sorted([], [1, 2, 3]))

    from solutions.arrays_3sum_closest import three_sum_closest
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
    print("three_sum_closest:", three_sum_closest([0, 0, 0], 1))

    from solutions.arrays_substring_concatenation import find_substring
    assert find_substring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]
    assert find_substring("a", ["a", "a"]) == []    # edge: not enough length
    print("find_substring:", find_substring("wordgoodgoodgoodbestword",
                                            ["word", "good", "best", "good"]))

    from solutions.arrays_first_missing_positive import first_missing_positive
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([1, 2, 3]) == 4   # edge: contiguous
    assert first_missing_positive([]) == 1
    print("first_missing_positive:", first_missing_positive([7, 8, 9, 11, 12]))

    from solutions.arrays_transpose_matrix import transpose
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([]) == []
    print("transpose:", transpose([[1], [2], [3]]))

# --------------------------------------------------------------------------- #
# Linked Lists
# --------------------------------------------------------------------------- #
def demo_linked_lists() -> None:
    section("LINKED LISTS")

    from solutions.linkedlist_singly import SinglyLinkedList
    sll = SinglyLinkedList()
    for v in (1, 2, 3):
        sll.append(v)
    sll.prepend(0)
    assert sll.to_list() == [0, 1, 2, 3]
    assert sll.delete(2) and sll.to_list() == [0, 1, 3]
    assert not sll.delete(99)                       # edge: delete missing
    print("singly list:", sll.to_list())

    from solutions.linkedlist_circular import has_cycle
    head = build_list([1, 2, 3, 4])
    assert not has_cycle(head)
    # Make a cycle: tail -> second node
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head.next
    assert has_cycle(head)
    print("has_cycle (looped):", has_cycle(head))

    from solutions.linkedlist_detect_cycle_start import detect_cycle_start
    # Reuse the looped list above; cycle starts at value 2.
    assert detect_cycle_start(head).val == 2
    tail.next = None                                # unlink to avoid side effects
    assert detect_cycle_start(head) is None         # edge: no cycle
    print("cycle start (acyclic):", detect_cycle_start(head))

    from solutions.linkedlist_reverse import reverse_list as reverse_ll
    assert to_pylist(reverse_ll(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert reverse_ll(None) is None                 # edge: empty list
    print("reverse:", to_pylist(reverse_ll(build_list([7, 8]))))

    from solutions.linkedlist_merge_k_sorted import merge_k_sorted
    lists = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_pylist(merge_k_sorted(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([None, None]) is None     # edge: all empty
    print("merge_k_sorted:", to_pylist(merge_k_sorted([build_list([2]), build_list([1])])))

    from solutions.linkedlist_remove_duplicates import remove_duplicates_sorted
    assert to_pylist(remove_duplicates_sorted(build_list([1, 1, 2, 3, 3]))) == [1, 2, 3]
    print("remove_dupes:", to_pylist(remove_duplicates_sorted(build_list([1, 1, 1]))))

    from solutions.linkedlist_find_middle import find_middle
    assert find_middle(build_list([1, 2, 3, 4, 5])).val == 3   # odd -> middle
    assert find_middle(build_list([1, 2, 3, 4])).val == 3      # even -> 2nd middle
    print("find_middle:", find_middle(build_list([10, 20, 30])).val)

    from solutions.linkedlist_add_two_numbers import add_two_numbers
    # 342 + 465 = 807, stored reversed.
    res = add_two_numbers(build_list([2, 4, 3]), build_list([5, 6, 4]))
    assert to_pylist(res) == [7, 0, 8]
    res2 = add_two_numbers(build_list([9, 9]), build_list([1]))  # edge: carry grows length
    assert to_pylist(res2) == [0, 0, 1]
    print("add_two_numbers:", to_pylist(res))

    from solutions.linkedlist_max_element import max_element as ll_max
    assert ll_max(build_list([3, 9, 2, 7])) == 9
    assert ll_max(None) is None                     # edge: empty
    print("ll max_element:", ll_max(build_list([1, 5, 5, 2])))

    from solutions.linkedlist_delete_last_occurrence import delete_last_occurrence
    assert to_pylist(delete_last_occurrence(build_list([1, 2, 3, 2, 4]), 2)) == [1, 2, 3, 4]
    assert to_pylist(delete_last_occurrence(build_list([1, 2]), 9)) == [1, 2]  # edge: absent
    print("delete_last_occurrence:",
          to_pylist(delete_last_occurrence(build_list([5, 5, 5]), 5)))


# --------------------------------------------------------------------------- #
# Stacks & Queues
# --------------------------------------------------------------------------- #
def demo_stacks_queues() -> None:
    section("STACKS & QUEUES")

    from solutions.stacks_stack import Stack
    st = Stack()
    assert st.pop() is None and st.peek() is None   # edge: empty ops
    for v in (1, 2, 3):
        st.push(v)
    assert st.peek() == 3 and st.pop() == 3 and len(st) == 2
    print("stack peek:", st.peek())

    from solutions.stacks_queue import Queue
    q = Queue()
    assert q.dequeue() is None                       # edge: empty
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.dequeue() == 2     # FIFO order
    print("queue dequeue:", q.dequeue())

    from solutions.stacks_circular_queue import CircularQueue
    cq = CircularQueue(2)
    assert cq.enqueue(1) and cq.enqueue(2)
    assert not cq.enqueue(3)                          # edge: full
    assert cq.dequeue() == 1 and cq.enqueue(3)        # wrap-around reuse
    print("circular queue peek:", cq.peek())

    from solutions.stacks_infix_to_postfix import infix_to_postfix
    assert infix_to_postfix("a+b*c") == "abc*+"
    assert infix_to_postfix("(a+b)*c") == "ab+c*"     # parentheses override
    print("infix->postfix 'a+b*(c-d)':", infix_to_postfix("a+b*(c-d)"))

    from solutions.stacks_next_greater_element import next_greater_elements
    assert next_greater_elements([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater_elements([5, 4, 3]) == [-1, -1, -1]   # edge: decreasing
    print("next_greater:", next_greater_elements([1, 3, 2, 4]))

    from solutions.stacks_delete_middle import delete_middle
    assert delete_middle([1, 2, 3, 4, 5]) == [1, 2, 4, 5]
    assert delete_middle([1]) == []                  # edge: single element
    print("delete_middle:", delete_middle([10, 20, 30, 40]))


def main() -> None:
    '''
    demo_strings()

    demo_math()

    demo_arrays()
    demo_linked_lists()
    demo_stacks_queues()
    demo_trees()
    demo_trie()
    demo_dp()
    demo_graph()
    '''
    demo_advanced()
    print(f"\n{'=' * 60}\nAll demos passed (Batch 1 + Batch 2).\n{'=' * 60}")


# --------------------------------------------------------------------------- #
# Trees & Binary Trees
# --------------------------------------------------------------------------- #
def demo_trees() -> None:
    section("TREES & BINARY TREES")

    from solutions.trees_height import height
    assert height(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert height(None) == 0                         # edge: empty
    assert height(build_tree([1])) == 1
    print("height:", height(build_tree([1, 2, 3, 4])))

    from solutions.trees_validate_bst import is_valid_bst
    assert is_valid_bst(build_tree([2, 1, 3]))
    assert not is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))  # 3 < 5 on right
    assert is_valid_bst(None)                         # edge: empty is valid
    print("is_valid_bst([10,5,15]):", is_valid_bst(build_tree([10, 5, 15])))

    from solutions.trees_traversals import inorder, preorder, postorder
    bst = build_tree([4, 2, 6, 1, 3, 5, 7])
    assert inorder(bst) == [1, 2, 3, 4, 5, 6, 7]      # BST inorder is sorted
    assert preorder(bst) == [4, 2, 1, 3, 6, 5, 7]
    assert postorder(bst) == [1, 3, 2, 5, 7, 6, 4]
    print("inorder:", inorder(bst))

    from solutions.trees_right_view import right_view
    assert right_view(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert right_view(None) == []                     # edge: empty
    print("right_view:", right_view(build_tree([1, 2, 3])))

    from solutions.trees_same_structure import is_same_tree
    assert is_same_tree(build_tree([1, 2, 3]), build_tree([1, 2, 3]))
    assert not is_same_tree(build_tree([1, 2]), build_tree([1, None, 2]))  # edge: shape
    print("is_same_tree:", is_same_tree(build_tree([1]), build_tree([1])))

    from solutions.trees_invert import invert_tree
    assert inorder(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9]))) == [9, 7, 6, 4, 3, 2, 1]
    print("invert (inorder):", inorder(invert_tree(build_tree([1, 2, 3]))))

    from solutions.trees_max_path_sum import max_path_sum
    assert max_path_sum(build_tree([1, 2, 3])) == 6
    assert max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert max_path_sum(build_tree([-3])) == -3       # edge: single negative
    print("max_path_sum:", max_path_sum(build_tree([2, -1, 3])))

    from solutions.trees_level_order import level_order
    assert level_order(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert level_order(None) == []
    print("level_order:", level_order(build_tree([1, 2, 3])))

    from solutions.trees_subtree import is_subtree
    assert is_subtree(build_tree([3, 4, 5, 1, 2]), build_tree([4, 1, 2]))
    assert not is_subtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
                          build_tree([4, 1, 2]))
    print("is_subtree:", is_subtree(build_tree([1, 1]), build_tree([1])))

    from solutions.trees_construct_pre_in import build_from_preorder_inorder
    rebuilt = build_from_preorder_inorder([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert level_order(rebuilt) == [[3], [9, 20], [15, 7]]
    print("construct (inorder of result):", inorder(rebuilt))

    from solutions.trees_kth_smallest_bst import kth_smallest
    tree = build_tree([5, 3, 7, 2, 4, 6, 8])
    assert kth_smallest(tree, 1) == 2 and kth_smallest(tree, 7) == 8
    assert kth_smallest(tree, 99) is None             # edge: out of range
    print("kth_smallest(k=3):", kth_smallest(tree, 3))


# --------------------------------------------------------------------------- #
# Trie
# --------------------------------------------------------------------------- #
def demo_trie() -> None:
    section("TRIE / PREFIX TREE")

    from solutions.trie_implement import Trie
    t = Trie()
    t.insert("apple")
    assert t.search("apple") and not t.search("app")  # prefix isn't a full word
    assert t.starts_with("app")                       # ...but is a valid prefix
    assert not t.starts_with("xyz")                   # edge: absent prefix
    t.insert("app")
    assert t.search("app")
    print("trie search 'apple':", t.search("apple"))

# --------------------------------------------------------------------------- #
# Dynamic Programming / Greedy
# --------------------------------------------------------------------------- #
def demo_dp() -> None:
    section("DYNAMIC PROGRAMMING / GREEDY")

    from solutions.dp_triplets import count_triplets_below_sum
    assert count_triplets_below_sum([-2, 0, 1, 3], 2) == 2   # (-2,0,1),(-2,0,3)
    assert count_triplets_below_sum([5, 1, 3, 4, 7], 12) == 4
    assert count_triplets_below_sum([1, 2], 5) == 0          # edge: <3 elements
    print("count_triplets_below_sum:", count_triplets_below_sum([1, 2, 3, 4], 8))

    from solutions.greedy_connect_ropes import min_cost_connect_ropes
    assert min_cost_connect_ropes([4, 3, 2, 6]) == 29
    assert min_cost_connect_ropes([5]) == 0                  # edge: one rope
    print("min_cost_connect_ropes:", min_cost_connect_ropes([1, 2, 3, 4, 5]))

    from solutions.dp_climb_stairs import count_ways_to_climb
    assert count_ways_to_climb(2) == 2 and count_ways_to_climb(5) == 8
    assert count_ways_to_climb(1) == 1
    print("count_ways_to_climb(10):", count_ways_to_climb(10))

    from solutions.dp_coin_change import coin_change
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1                         # edge: impossible
    assert coin_change([1], 0) == 0
    print("coin_change([1,2,5], 7):", coin_change([1, 2, 5], 7))

    from solutions.dp_knapsack import knapsack_01
    assert knapsack_01([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
    assert knapsack_01([5], [10], 3) == 0                    # edge: nothing fits
    print("knapsack_01:", knapsack_01([2, 3, 4], [4, 5, 6], 5))

    from solutions.dp_dice_throw import count_dice_ways
    assert count_dice_ways(2, 6, 7) == 6
    assert count_dice_ways(1, 6, 3) == 1
    assert count_dice_ways(2, 6, 1) == 0                     # edge: unreachable
    print("count_dice_ways(3,6,8):", count_dice_ways(3, 6, 8))

    from solutions.dp_lis import longest_increasing_subsequence
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert longest_increasing_subsequence([]) == 0           # edge: empty
    assert longest_increasing_subsequence([7, 7, 7]) == 1    # strict: ties don't extend
    print("LIS:", longest_increasing_subsequence([0, 1, 0, 3, 2, 3]))

    from solutions.dp_egg_drop import egg_drop
    assert egg_drop(2, 10) == 4
    assert egg_drop(1, 10) == 10                             # edge: one egg -> linear
    print("egg_drop(2, 36):", egg_drop(2, 36))

    from solutions.dp_matrix_chain import matrix_chain_order
    assert matrix_chain_order([40, 20, 30, 10, 30]) == 26000
    assert matrix_chain_order([10, 20]) == 0                 # edge: single matrix
    print("matrix_chain_order:", matrix_chain_order([1, 2, 3, 4]))

    from solutions.dp_combination_sum import combination_sum
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2], 1) == []                     # edge: impossible
    print("combination_sum([2,3,5], 8):", combination_sum([2, 3, 5], 8))

    from solutions.dp_house_robber import max_stolen_value
    assert max_stolen_value([2, 7, 9, 3, 1]) == 12
    assert max_stolen_value([]) == 0                         # edge: no houses
    assert max_stolen_value([5]) == 5
    print("max_stolen_value:", max_stolen_value([2, 1, 1, 2]))

    from solutions.dp_decode_ways import count_decodings
    assert count_decodings("226") == 3
    assert count_decodings("06") == 0                        # edge: leading zero
    assert count_decodings("10") == 1
    print("count_decodings('11106'):", count_decodings("11106"))

    from solutions.dp_unique_paths_obstacles import unique_paths_with_obstacles
    assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths_with_obstacles([[1]]) == 0           # edge: blocked start
    print("unique_paths_with_obstacles:",
          unique_paths_with_obstacles([[0, 0], [0, 0]]))

    from solutions.dp_jump_game import can_jump
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])                     # edge: stuck at the 0
    print("can_jump([0]):", can_jump([0]))

    from solutions.dp_rod_cutting import rod_cutting
    assert rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22
    assert rod_cutting([2, 5, 7, 8], 5) == 12
    print("rod_cutting:", rod_cutting([3, 5, 8, 9], 4))

    from solutions.dp_max_product_cutting import max_product_after_cutting
    assert max_product_after_cutting(10) == 36
    assert max_product_after_cutting(2) == 1                 # edge: forced 1+1
    print("max_product_after_cutting(8):", max_product_after_cutting(8))

    from solutions.dp_count_ways_distance import count_ways_to_cover_distance
    assert count_ways_to_cover_distance(3) == 4              # 1+1+1, 1+2, 2+1, 3
    assert count_ways_to_cover_distance(0) == 1
    print("count_ways_to_cover_distance(4):", count_ways_to_cover_distance(4))


# --------------------------------------------------------------------------- #
# Graph / Matrix
# --------------------------------------------------------------------------- #
def demo_graph() -> None:
    section("GRAPH / MATRIX")

    from solutions.graph_number_of_islands import num_islands
    grid = [["1", "1", "0", "0"], ["1", "0", "0", "1"], ["0", "0", "1", "1"]]
    assert num_islands([row[:] for row in grid]) == 2
    assert num_islands([["0"]]) == 0                         # edge: no land
    print("num_islands:", num_islands([row[:] for row in grid]))

    from solutions.graph_flood_fill import flood_fill
    assert flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == \
        [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    print("flood_fill:", flood_fill([[0, 0], [0, 0]], 0, 0, 5))

    from solutions.graph_largest_region import largest_region
    assert largest_region([[0, 0, 1], [1, 1, 0], [0, 1, 0]]) == 4   # 8-directional
    print("largest_region:", largest_region([[1, 0], [0, 1]]))      # diagonal joins

    from solutions.graph_detect_cycle_directed import has_cycle_directed
    assert has_cycle_directed({0: [1], 1: [2], 2: [0]}, 3)
    assert not has_cycle_directed({0: [1], 1: [2]}, 3)              # edge: DAG
    print("has_cycle_directed:", has_cycle_directed({0: [1], 1: [1]}, 2))  # self-loop

    from solutions.graph_bipartite import is_bipartite
    assert is_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}, 4)   # even cycle
    assert not is_bipartite({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 3)          # triangle
    print("is_bipartite:", is_bipartite({0: [1], 1: [0]}, 2))

    from solutions.graph_bridges import find_bridges
    bridges = find_bridges({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}, 4)
    assert set(bridges) == {(0, 1), (1, 2), (2, 3)}                 # a path: all bridges
    no_bridges = find_bridges({0: [1, 2], 1: [0, 2], 2: [0, 1]}, 3) # triangle: none
    assert no_bridges == []
    print("find_bridges:", find_bridges({0: [1], 1: [0]}, 2))

    from solutions.graph_snake_ladder import snakes_and_ladders
    # 9-square board, ladder 2->6, snake 8->1.
    assert snakes_and_ladders(9, {2: 6, 8: 1}) >= 1
    assert snakes_and_ladders(6, {}) == 1                          # one roll reaches 6
    print("snakes_and_ladders:", snakes_and_ladders(9, {2: 6, 8: 1}))

    from solutions.graph_petrol_pump_tour import first_circular_tour
    assert first_circular_tour([(4, 6), (6, 5), (7, 3), (4, 5)]) == 1
    assert first_circular_tour([(1, 5), (2, 3)]) == -1            # edge: impossible
    print("first_circular_tour:", first_circular_tour([(6, 4), (3, 6), (7, 3)]))


# --------------------------------------------------------------------------- #
# Advanced
# --------------------------------------------------------------------------- #
def demo_advanced() -> None:
    section("ADVANCED")

    from solutions.advanced_nary_tree_mirror import NaryNode, is_mirror_of_itself
    #        1
    #      / | \
    #     2  3  2     (children mirror around the center)
    symmetric = NaryNode(1, [NaryNode(2), NaryNode(3), NaryNode(2)])
    assert is_mirror_of_itself(symmetric)
    asymmetric = NaryNode(1, [NaryNode(2), NaryNode(3), NaryNode(4)])
    assert not is_mirror_of_itself(asymmetric)
    assert is_mirror_of_itself(None)                              # edge: empty
    print("is_mirror_of_itself:", is_mirror_of_itself(symmetric))


if __name__ == "__main__":
    main()
