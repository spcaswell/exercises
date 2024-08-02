"""
A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array
together at any location.



Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.



Constraints:

    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

"""

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Count number of 1s, Create sliding window of size equal to number of 1s
        # Scan the array with the window.  The windows with the least 0s is equal to the minimum number of swaps.

        win_size = sum(nums)  # It's 0's and 1's so the sum is the total number of 1's
        min_swaps = float("inf")

        nums2 = nums.copy()
        nums2.extend(nums[:win_size])  # Add the window size to the end of the array to account for wrap-around

        for start in range(len(nums)):
            end = start + win_size
            min_swaps = min(min_swaps, win_size - sum(nums2[start:end]))  # scan for smallest number of 0s in window
        return min_swaps


if __name__ == "__main__":
    s = Solution()

    nums = [0, 1, 0, 1, 1, 0, 0]
    print(s.minSwaps(nums))

    nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    print(s.minSwaps(nums))

    nums = [1, 1, 0, 0, 1]
    print(s.minSwaps(nums))

    nums = [1, 0, 0, 1, 1, 0, 1, 1]
    print(s.minSwaps(nums))
