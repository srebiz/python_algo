from typing import List


def flood_fill(image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
    """
    Recolor the region connected to (sr, sc) sharing its original color.

    DFS from the seed; the no-op guard (color already == new_color) prevents
    infinite recursion.

    Time:  O(m * n).  Space: O(m * n) recursion worst case.
    """
    rows, cols = len(image), len(image[0])
    start = image[sr][sc]
    if start == new_color:
        return image

    def fill(r: int, c: int) -> None:
        if 0 <= r < rows and 0 <= c < cols and image[r][c] == start:
            image[r][c] = new_color
            fill(r + 1, c); fill(r - 1, c); fill(r, c + 1); fill(r, c - 1)

    fill(sr, sc)
    return image
