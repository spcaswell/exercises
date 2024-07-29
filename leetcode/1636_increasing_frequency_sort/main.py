"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.



Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]


Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency_count = {}
        for x in nums:
            if x in frequency_count:
                frequency_count[x] += 1
            else:
                frequency_count[x] = 1
        sorted_by_frequency = sorted(frequency_count, key=lambda x: (frequency_count[x], -x))
        to_return = []
        for x in sorted_by_frequency:
            while frequency_count[x] > 0:
                to_return.append(x)
                frequency_count[x] -= 1
        return to_return

    def frequencySort2(self, nums: List[int]) -> List[int]:
        """
        Use Counter from collections
        :param nums:
        :return:
        """
        from collections import Counter
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort([1,1,2,2,2,3]))
    print(s.frequencySort2([1, 1, 2, 2, 2, 3]))

    print(s.frequencySort([2,3,1,3,2]))
    print(s.frequencySort2([2, 3, 1, 3, 2]))

    print(s.frequencySort([-1,1,-6,4,5,-6,1,4,1]))
    print(s.frequencySort2([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
