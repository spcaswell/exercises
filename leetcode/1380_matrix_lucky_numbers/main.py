"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:

Input: matrix = [[3,7,8],
                [9,11,13],
                [15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],
                [9,3,8,7],
                [15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],
                [1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.


Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
"""

from typing import List


class Solution:
    def luckyNumbers2(self, matrix: List[List[int]]) -> List[int]:
        """
        The main idea is to find common elements in the minimum values per row (map(min,matrix)) and maximum per column (map(max,zip(*matrix))) using the intersection operator & between sets.

        The first set is generated using the map(fn, iter) function. It applies the function fn to the iterable iter. In the case of map(min,matrix), it will return the
        minimum of each row of matrix.

        To obtain the columns instead of the rows, the second set uses the zip(i1, i2, ...) function which processes iterables ix in parallel, producing tuples with an item from each one.
        These iterables are the rows of the matrix, using the unpacking operator * to get all the rows: zip(*matrix). Then, similar to the first set, it applies the max to each column.
        :param matrix:
        :return:
        """
        return list(set(map(min, matrix)) & set(map(max, zip(*matrix))))

    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        MATRIX_HEIGHT = len(matrix)  # Rows, x coordinate
        MATRIX_LENGTH = len(matrix[0])  # Columns, y coordinate
        row_minimus = []
        for x in range(MATRIX_HEIGHT):
            current_min = (x, 0)
            current_min_value = matrix[x][0]
            for y in range(1, MATRIX_LENGTH):
                if matrix[x][y] < current_min_value:
                    current_min = (x, y)
                    current_min_value = matrix[x][y]
            row_minimus.append(current_min)

        for candidate in row_minimus[:]:  # Use slice to create a copy of the list to iterate over so modificatoins don't screw up the iteration.
            x = candidate[0]
            y = candidate[1]
            current_max = matrix[x][y]
            for row_index in range(MATRIX_HEIGHT):
                if matrix[row_index][y] > current_max:
                    row_minimus.remove(candidate)
                    break

        lucky_numbers = []
        for x, y in row_minimus:
            lucky_numbers.append(matrix[x][y])
        return lucky_numbers


if __name__ == "__main__":
    s = Solution()

    matrix1 = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(s.luckyNumbers(matrix1))  # 15 is lucky

    matrix2 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]
    print(s.luckyNumbers(matrix2))  # 12 is lucky

    matrix3 = [[7, 8], [1, 2]]
    print(s.luckyNumbers(matrix3)) # 7 is lucky
