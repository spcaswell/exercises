"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]
Output: 7


Constraints:

    0 <= nums.length <= 1000
    -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(N) time and space complexity
        max_length = 0
        s = set(nums)  # use a set to speed up membership checks
        for x in s:
            if x-1 not in s:
                length = 1
                while (x+length) in s:  # since length increases by 1 each time we can use it to check for the next sequence value
                    length += 1
                max_length = max(max_length, length)
        return max_length


if __name__ == "__main__":
    s = Solution()

    nums = [2, 20, 4, 10, 3, 4, 5]
    print(s.longestConsecutive(nums))

    nums = [0, 3, 2, 5, 4, 6, 1, 1]
    print(s.longestConsecutive(nums))
