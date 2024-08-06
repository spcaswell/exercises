"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].



Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.
"""


from typing import List


class Solution():
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Standard Brute Force Approach
        # for x in range(len(numbers)):
        #     for j in range(len(numbers)):
        #         if j == x:
        #             continue
        #         if numbers[j] + numbers[x] == target:
        #             return [x+1, j+1]

        # But the array is sorted!
        l, r = 0, len(numbers) - 1  # set start points to the ends of the list

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:  # too big make the right operand smaller
                r -= 1
            elif curSum < target:  # too small make the left operand bigger
                l += 1
            else:
                return [l + 1, r + 1]  # match!



if __name__ == "__main__":
    s = Solution()

    numbers = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
    print(s.twoSum(numbers, target))

    numbers = [-1, 0]
    target = -1
    print(s.twoSum(numbers, target))
