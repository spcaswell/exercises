"""
You start at the cell (rStart, cStart) of a rows x cols grid facing east. The northwest corner is at the first row and
column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's
boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all
rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.


Example 1:
        ---->-------v---v---v
        |           |   |   |
        ^    |1|-> |2| |3| |4|
        |           |   |   |
        ------<-----<---<---<

Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]

Example 2:

Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]



Constraints:

    1 <= rows, cols <= 100
    0 <= rStart < rows
    0 <= cStart < cols
"""


from typing import List


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        """
        The distance moved in a single direction in a spiral traversal increases by one for every two moves.
        Move right 1, move down 1, move left 2, move up 2, move right 3...
        Keep track of the number of valid coordinates we've encountered, and when that equals the total number of
        valid coordinates we're done.

        Let N be the number of Rows and M be the number of Columns
        O(max(N,M)^2) time complexity
        O(N*M) for the result array in extra space

        :param rows: Number of rows in matrix
        :param cols: Number of columns in matrix
        :param rStart: The starting row coordinate
        :param cStart: The starting column coordinate
        :return: A list of rows in the order visited moving in a clockwise sprial from the starting indexes
        """
        move_distance = 0
        cells = rows * cols  # Just do this multiplication once instead of every outer loop
        res = [[rStart, cStart]]  # The starting position is guaranteed to be valid

        while len(res) < cells:
            move_distance += 1
            for i in range(move_distance):
                cStart += 1  # Move right
                if (0 <= cStart < cols) and (0 <= rStart < rows):
                    res.append([rStart, cStart])
            for j in range(move_distance):
                rStart += 1  # Move Down
                if (0 <= cStart < cols) and (0 <= rStart < rows):
                    res.append([rStart, cStart])
            move_distance += 1
            for i in range(move_distance):
                cStart -= 1  # Move Left
                if (0 <= cStart < cols) and (0 <= rStart < rows):
                    res.append([rStart, cStart])
            for j in range(move_distance):
                rStart -= 1  # Move Up
                if (0 <= cStart < cols) and (0 <= rStart < rows):
                    res.append([rStart, cStart])
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.spiralMatrixIII(1, 4, 0, 0))
    print(s.spiralMatrixIII(5, 6, 1, 4))
