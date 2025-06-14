"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]



Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        """
        Use a hashmap to run in O(N) time, but O(N) extra space
        :param nums: The array of numbers
        :param target: The target sum
        :return: The indexes of the values in nums that add up to target.
        """
        seen = {}
        pairs = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                pairs.append((seen[diff], i))
            seen[n] = i
        return pairs

    def slow_twoSum(self, nums: List[int], target: int)  -> List[int]:
        """
        O(N^2) time complexity, but no additional memory
        :param nums: The array of numbers
        :param target: The target sum
        :return: The indexes of the first values in nums found that add up to target.
        """
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


if __name__ == "__main__":
    s = Solution()

    nums = [2, 7, 11, 15, 0, 9]
    print(s.slow_twoSum(nums, 9))
    print(s.twoSum(nums, 9))

    nums = [3, 2, 4]
    print(s.slow_twoSum(nums, 6))

    nums = [3, 3]
    print(s.slow_twoSum(nums, 6))
