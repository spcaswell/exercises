"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both
diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.



Example 1:

    4  3  8  4
    9  5  1  9
    2  7  6  2

Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:

    4  3  8
    9  5  1
    2  7  6

while this one is not:

    3  8  4
    5  1  9
    7  6  2

In total, there is only one magic square inside the given grid.

Example 2:

Input: grid = [[8]]
Output: 0



Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 10
    0 <= grid[i][j] <= 15
"""

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        Generate all possible 3x3 grids then check them for magic square properties
        O(M*N) time complexity because the number of squares is linearly proportional to the size of the matrix (M*N)
        O(M*N) extra space for the same reason as I'm storing a list of sub-squares

        :param grid: The matrix to check for magic squares
        :return: Integer of how many magic squares are found in grid
        """
        sub_grids = []
        row = len(grid)
        col = len(grid[0])

        for start_row in range(row - 3 + 1):
            for start_col in range(col - 3 + 1):
                # Creating 3 * 3 matrix
                # List comprehension for extracting 3x3 sub-matrices
                sub_grid = [row[start_col: start_col + 3] for row in grid[start_row: start_row + 3]]
                sub_grids.append(sub_grid)

        return self.magicGrid(sub_grids)

    def magicGrid(self, grids: List[List[List[int]]]) -> int:
        # Visual representations makes it easier to understand
        # All of this can be derived with only one known position and a couple of loops for a more general solution
        # This approach would also allow for O(1) memory space

        count = 0
        magic_sum = 15

        for grid in grids:
            # grid is 3 * 3 matrix
            a, b, c = grid[0]
            d, e, f = grid[1]
            g, h, i = grid[2]

            # Row Sum
            row_sum1 = a + b + c
            row_sum2 = d + e + f
            row_sum3 = g + h + i

            # Column Sum
            col_sum1 = a + d + g
            col_sum2 = b + e + h
            col_sum3 = c + f + i

            # Diagonal Sum
            diag_sum1 = a + e + i
            diag_sum2 = g + e + c

            all_numbers = [a, b, c, d, e, f, g, h, i]
            # Check for Uniqueness
            if len(set(all_numbers)) == 9 and all(1 <= num <= 9 for num in all_numbers):
                if row_sum1 == row_sum2 == row_sum3 == col_sum1 == col_sum2 == col_sum3 == diag_sum1 == diag_sum2 == magic_sum:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()

    print(s.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
    print(s.numMagicSquaresInside([[8]]))
    print(s.numMagicSquaresInside([[1, 2, 3], [4, 5, 12], [9, 10, 15]]))
    print(s.numMagicSquaresInside([[1, 2, 3], [4, 5, 1], [9, 10, 15], [2, 7, 8]]))
