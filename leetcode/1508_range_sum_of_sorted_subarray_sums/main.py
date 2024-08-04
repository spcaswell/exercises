"""
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous
subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the
answer can be a huge number return it modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the
 new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13.

Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of
 the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.

Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50



Constraints:

    n == nums.length
    1 <= nums.length <= 1000
    1 <= nums[i] <= 100
    1 <= left <= right <= n * (n + 1) / 2

"""

from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        O(N^2 log N)  It's slow but it does the job.  Space complexity is O(N^2).
        :param nums:
        :param n:
        :param left:
        :param right:
        :return:
        """
        new_array = []
        for i in range(len(nums)):
            new_array.append(nums[i])
            for j in range(i+1, len(nums)):
                new_array.append(sum(nums[i:j+1]))
        new_array.sort()
        mod = 10**9 + 7
        return sum(new_array[left-1:right]) % mod

    def rangeSum2(self, nums, n, left, right):
        """
        O(N^2 log N) again for time, but space is O(N)
        :param nums:
        :param n:
        :param left:
        :param right:
        :return:
        """
        import heapq
        pq = []
        for i in range(n):
            heapq.heappush(pq, (nums[i], i))

        ans = 0
        mod = 1e9 + 7
        for i in range(1, right + 1):
            p = heapq.heappop(pq)
            # If the current index is greater than or equal to left, add the
            # value to the answer.
            if i >= left:
                ans = (ans + p[0]) % mod
            # If index is less than the last index, increment it and add its
            # value to the first pair value.
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heapq.heappush(pq, p)
        return int(ans)


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 4]
    n, left, right = 4, 1, 5
    print(s.rangeSum(nums, n, left, right))

    n, left, right = 4, 3, 4
    print(s.rangeSum(nums, n, left, right))

    n, left, right = 4, 1, 10
    print(s.rangeSum(nums, n, left, right))
