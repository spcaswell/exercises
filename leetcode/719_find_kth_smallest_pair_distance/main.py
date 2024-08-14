"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j]
where 0 <= i < j < nums.length.

Example 1:

Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:

Input: nums = [1,1,1], k = 2
Output: 0

Example 3:

Input: nums = [1,6,1], k = 3
Output: 5

Constraints:

    n == nums.length
    2 <= n <= 104
    0 <= nums[i] <= 106
    1 <= k <= n * (n - 1) / 2
"""


from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        O(n log n + n log M) time complexity: sort of nums + binary search over prefix_count and value_count which is
        dependent on the max_distance (M)

        O(2n+M) space complexity: n for value_count and sorting, M for prefix_count.
        :param nums:
        :param k:
        :return:
        """
        nums.sort()
        size = len(nums)
        max_value = nums[-1]
        max_distance = max_value+1
        prefix_count = [0] * max_distance
        value_count = [0] * (max_value + 1)

        index = 0
        for value in range(max_distance):
            while index < size and nums[index] <= value:
                index += 1
            prefix_count[value] = index
        for i in range(size):
            value_count[nums[i]] += 1

        # Binary search to find kth smallest distance
        left, right = 0, max_value
        while left < right:
            mid = (left + right) // 2

            # Count pairs with distance <= mid
            count = self._count_pairs(nums, prefix_count, value_count, mid)

            # Adjust binary search bounds based on count
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def _count_pairs(self, nums, prefix_count, value_count, max_distance):
        count = 0
        array_size = len(nums)
        index = 0

        while index < array_size:
            current_value = nums[index]
            value_count_for_current = value_count[current_value]

            # Calculate pairs involving current value with distance <= max_distance
            pairs_with_larger_values = (
                    prefix_count[
                        min(current_value + max_distance, len(prefix_count) - 1)
                    ]
                    - prefix_count[current_value]
            )
            pairs_with_same_values = (
                    value_count_for_current * (value_count_for_current - 1) // 2
            )
            count += (
                    pairs_with_larger_values * value_count_for_current
                    + pairs_with_same_values
            )

            # Skip duplicate values
            while index + 1 < array_size and nums[index] == nums[index + 1]:
                index += 1
            index += 1

        return count



    def smallestDistancePair_slow(self, nums: List[int], k: int) -> int:
        """
        O(N^2) time and space complexity
        :param nums:
        :param k:
        :return:
        """
        distances = []
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                distances.append(abs(nums[i] - nums[j]))
        distances.sort()
        return distances[k-1]



if __name__ == "__main__":
    s = Solution()

    print(s.smallestDistancePair(nums=[62, 100, 4], k=1))
    print(s.smallestDistancePair(nums=[1, 1, 1], k=2))
    print(s.smallestDistancePair(nums=[1, 6, 1], k=3))
