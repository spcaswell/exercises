"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These
characters divide the square into contiguous regions.

Given a grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:

    |------|
    |    / |
    |  /   |
    |/-----|

Input: grid = [" /","/ "]
Output: 2

Example 2:

    |------|
    |    / |
    |      |
    |------|

Input: grid = [" /","  "]
Output: 1

Example 3:

     |-----|
     |  /\ |
     | /  \|
     | \  /|
     | \ / |
     |-----|

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 30
    grid[i][j] is either '/', '\', or ' '.
"""


from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = {}

        # Initialize the union-find parent for each triangle
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        # Each cell is represented by 4 triangles: 0 (top-left), 1 (top-right), 2 (bottom-right), 3 (bottom-left)
        def get_index(i, j, k):
            return (i * n + j) * 4 + k

        # Initialize all triangles
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    parent[get_index(i, j, k)] = get_index(i, j, k)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    union(get_index(i, j, 0), get_index(i, j, 3))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                elif grid[i][j] == '\\':
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 2), get_index(i, j, 3))
                else:
                    union(get_index(i, j, 0), get_index(i, j, 1))
                    union(get_index(i, j, 1), get_index(i, j, 2))
                    union(get_index(i, j, 2), get_index(i, j, 3))

                # Union with right and bottom cells if possible
                if j + 1 < n:
                    union(get_index(i, j, 1), get_index(i, j + 1, 3))
                if i + 1 < n:
                    union(get_index(i, j, 2), get_index(i + 1, j, 0))

        # Count the number of distinct roots
        return sum(find(x) == x for x in parent)


if __name__ == "__main__":
    s = Solution()

    print(s.regionsBySlashes([" /", "/ "]))
    print(s.regionsBySlashes([" /", "  "]))
    print(s.regionsBySlashes(["/\\", "\\/"]))
