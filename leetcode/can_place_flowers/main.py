"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot
be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # check if at first element or previous element
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                # check if at last element or next element
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                # if both are empty, plant a flower and count it.
                if empty_right and empty_left:
                    flowerbed[i] = 1
                    count += 1
        # Did we plant at least as many flowers as n?
        return count >= n


if __name__ == "__main__":
    s = Solution()
    print(s.canPlaceFlowers([1,0,0,0,1], 1))
    print(s.canPlaceFlowers([1, 0, 0, 0, 1], 2))
