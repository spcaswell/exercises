"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

       8              8     7
       |  6           |     |
       |  |     5  4  |     |
       |  |  2  |  |  |  3  |
    1  |  |  |  |  |  |  |  |


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(i=1 and i=8) the container can contain is 49 ( (8-1)*7 or width*height).

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Use two pointers on each end and shift whichever is smallest to the next bar and see if the area is larger
        # return the largest area found
        # O(N) time and O(1) space
        i = 0
        j = len(height) - 1

        max_area = 0
        while i < j:
            max_area = max(min(height[i], height[j]) * (j-i), max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()

    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(s.maxArea([1, 1]))
