"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.



Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort it and use twoSumII approach
        # O(N^2) time and O(1)/O(N) space depending on sort implementation
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break  # positive numbers can never sum to 0

            if i > 0 and a == nums[i - 1]:  # skip combinations already seen
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                triplet = a + nums[l] + nums[r]
                if triplet > 0:
                    r -= 1  # Check next smaller value
                elif triplet < 0:
                    l += 1  # Check next larger value
                else:
                    res.append([a, nums[l], nums[r]])  # It equals 0; add it and check for other combos
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1  # skip any already seen combos
        return res

    def threeSumSlow(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            doublets = self.twoSum(nums, -nums[i], i)
            if doublets:
                for x in doublets:
                    if i not in x:
                        triplet = [nums[i], nums[x[0]], nums[x[1]]]
                        triplet.sort()
                        if triplet not in res:
                            res.append(triplet)
        return res

    def twoSum(self, nums: List[int], target: int, skip_index: int) -> List[List[int]]:
        """
        Use a hashmap to run in O(N) time, but O(N) extra space
        :param nums: The array of numbers
        :param target: The target sum
        :param skip_index: an index to ignore
        :return: The indexes of the values in nums that add up to target.
        """
        seen = {}
        res = []
        for i, n in enumerate(nums):
            if i == skip_index:
                continue
            diff = target - n
            if diff in seen:
                res.append([seen[diff], i])
            seen[n] = i
        return res






if __name__ == "__main__":
    s = Solution()

    nums = [0, 0, 0, 0]
    print(s.threeSum(nums))

    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))

    nums = [0, 1, 1]
    print(s.threeSum(nums))

    nums = [0, 0, 0]
    print(s.threeSum(nums))
