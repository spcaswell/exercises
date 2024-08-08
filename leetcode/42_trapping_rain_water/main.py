"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.

Example 1:

       |
   |www||w|
_|w||w||||||

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (w's) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
"""


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(N) time, O(1) space

        l and r are pointers to the left and right ends of the array.
        min(l_max, r_max) - height[i]; where i is either l or r depending on if your using l_max or r_max respectively
        gives the amount of water that can be stored at i
        :param height: the elevation map
        :return:
        """
        trapped = 0
        if not height:
            return trapped

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                trapped += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                trapped += r_max - height[r]

        return trapped


if __name__ == "__main__":
    s = Solution()

    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap([4, 2, 0, 3, 2, 5]))
    print(s.trap([1, 2, 3, 3, 2, 1]))
    print(s.trap([5, 4, 0, 4, 5]))
