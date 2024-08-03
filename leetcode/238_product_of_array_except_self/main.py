"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""
from typing import List

class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            """
            This is a O(N) time solution that runs in O(1) space, since the output array is not considered extra in
            the context of this problem.
            :param nums: The array containing numbers to multiply.
            :return:
            """
            res = [1] * len(nums)  # initialize result array to 1

            # Compute prefix values into output array.  The prefix is all values in nums multiplied together to the left
            # of the current index.
            for i in range(1, len(nums)):  # leave res[0] alone as the first prefix value is always 1.
                res[i] = res[i-1] * nums[i-1]

            # set postfix value to 1
            postfix =1  # the first postfix value is 1

            # Now multiply all prefix values by the appropriate postfix value.  The postfix is all values in nums
            # multiplied together to the right of the current index.
            for i in range(len(nums) - 1, -1, -1):
                res[i] *= postfix
                postfix *= nums[i]
            return res


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))

    nums = [-1, 1, 0, -3, 3]
    print(s.productExceptSelf(nums))
