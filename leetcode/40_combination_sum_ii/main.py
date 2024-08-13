"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]



Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [i for i in candidates if i <= target]  # Cull the list of all nums larger than target.  You can never sum values > target to = target.

        candidates.sort()

        dp = [set() for _ in range(target + 1)]
        dp[0].add(())

        for i, c in enumerate(candidates):

            # Build all combos that sum to each value less than equal target
            for j in range(target - c, -1, -1):
                for tup in dp[j]:
                    dp[j + c].add(tuple(list(tup) + [c]))

        # return the list of combinations that sum to target
        return list(dp[target])

if __name__ == "__main__":
    s = Solution()

    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))
