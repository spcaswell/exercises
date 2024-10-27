"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Brute force solution
        O(min(row,col)*row*col) time complexity
        O(row*col) extra space for a copy of the matrix when checking the whole thing.  Each square is thrown out
        after use.

        :param matrix:
        :return: number of square sub-matrices containing only ones
        """
        size = 1
        row = len(matrix)
        col = len(matrix[0])
        max_size = min(row, col)
        count = 0

        while size <= max_size:
            for start_row in range(row - size + 1):
                for start_col in range(col - size + 1):
                    # Creating size * size matrix
                    # List comprehension for extracting size*size sub-matrix
                    sub_grid = [row[start_col: start_col + size] for row in matrix[start_row: start_row + size]]
                    skip = False
                    for r in sub_grid:
                        if 0 in r:
                            skip = True
                            break
                    if skip:
                        continue
                    count += 1
            size += 1
        return count

    def countSquares_faster(self, matrix: List[List[int]]) -> int:
        """Bottom Up DP approach with Space Complexity O(col) where col is the number of columns in the matrix.
        We only need the current row and the previous row at one time
        O(Rows * Cols) Time complexity
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        prev = [0] * (1 + COLS)
        result = 0

        for i in range(ROWS):
            curr = [0] * (1 + COLS)
            for j in range(1, 1 + COLS):
                if matrix[i][j - 1] == 1:
                    curr[j] = 1 + min(curr[j - 1], prev[j - 1], prev[j])
            result += sum(curr)
            prev = curr
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]))
    print(s.countSquares([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
