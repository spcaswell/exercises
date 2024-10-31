"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.

You can start at any cell in the first column of the matrix, and traverse the grid in the following way:

    From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1)
    such that the value of the cell you move to, should be strictly bigger than the value of the current cell.

Return the maximum number of moves that you can perform.



Example 1:

    2  4  3  5
    5  4  9  3
    3  4  2  11
    10 9  13 15

Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

Example 2:

    3  2  4
    2  1  9
    1  1  7


Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.


Constraints:

    m == grid.length
    n == grid[i].length
    2 <= m, n <= 1000
    4 <= m * n <= 105
    1 <= grid[i][j] <= 106
"""

from typing import List


class Solution:
    def maxMoves_dfs(self, grid: List[List[int]]) -> int:
        """
        DFS implementation with memorization optimization
        O(M*N) time and space

        :param grid:
        :return:
        """
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Directions for possible moves: (row offset, col offset)
        directions = [(-1, 1), (0, 1), (1, 1)]

        # Memoization cache to store the max moves from each cell
        memo = {}

        # Helper function to perform DFS with memoization
        def dfs(row, col):
            # If we are at the last column, no further moves are possible
            if col == n - 1:
                return 0
            # If already computed, return the stored result
            if (row, col) in memo:
                return memo[(row, col)]

            max_moves = 0
            current_value = grid[row][col]

            # Check all possible moves
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Check if the move is valid
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > current_value:
                    # Calculate moves from the next cell
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))

            # Store the result in memo
            memo[(row, col)] = max_moves
            return max_moves

        # Try to start from each cell in the first column and find the max moves
        result = 0
        for i in range(m):
            result = max(result, dfs(i, 0))

        return result


