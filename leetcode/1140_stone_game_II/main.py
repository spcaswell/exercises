"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile
has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then,
we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again.
Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all
three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104



Constraints:

    1 <= piles.length <= 100
    1 <= piles[i] <= 104
"""


from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        O(N^3) time; O(N^2) space
        :param piles:
        :return:
        """
        l = len(piles)

        dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]  # 2D list comprehension; init all values to 0

        # Calculate the suffix sums of the stone piles and store in the final column of the dp
        # suffix_sum = [0 for _ in range(l+1)]
        # for i in range(l-1, -1, -1):
        #     suffix_sum[i] = piles[i] + suffix_sum[i+1]

        for i in range(l - 1, -1, -1):  # or just do it directly in the dp table
            dp[i][l] = piles[i] + dp[i+1][l]

        # Tabulate possibilities
        for i in range(l - 1, -1, -1):
            for max_until_now in range(l - 1, 0, -1):
                for p in range(1, min(2*max_until_now, l - i) + 1):
                    dp[i][max_until_now] = max(dp[i][max_until_now], dp[i][l] - dp[i+p][max(max_until_now, p)])

        # return max first player can achieve
        return dp[0][1]


if __name__ == "__main__":
    s = Solution()
    print(s.stoneGameII(piles=[2, 7, 9, 4, 4]))
    print(s.stoneGameII(piles=[1, 2, 3, 4, 5, 100]))