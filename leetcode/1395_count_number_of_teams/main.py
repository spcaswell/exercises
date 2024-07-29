"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

    Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
    A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4



Constraints:

    n == rating.length
    3 <= n <= 1000
    1 <= rating[i] <= 105
    All the integers in rating are unique.

"""

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # O(N^3) is quite slow...
        rating_length = len(rating)
        teams = 0
        for i in range(rating_length-2):

            for j in range(i+1, rating_length-1):

                for k in range(j+1, rating_length):
                    c = (rating[i], rating[j], rating[k])
                    if rating[i] > rating[j] > rating[k]:
                        teams += 1
                    if rating[i] < rating[j] < rating[k]:
                        teams += 1
        return teams

    def numTeams2(self, rating: List[int]) -> int:
        # Improve to O(N^2)
        N = len(rating)
        teams = 0
        for j in range(1, N - 1):
            smaller_left = bigger_left = smaller_right = bigger_right = 0
            for i in range(j):
                smaller_left += rating[i] < rating[j]
                bigger_left += rating[i] > rating[j]
            for k in range(j + 1, N):
                smaller_right += rating[k] < rating[j]
                bigger_right += rating[k] > rating[j]
            teams += smaller_left * bigger_right
            teams += bigger_left * smaller_right
        return teams


if __name__ == "__main__":
    s = Solution()

    rating = [2, 5, 3, 4, 1]
    print(s.numTeams(rating))

    rating = [2, 1, 3]
    print(s.numTeams(rating))

    rating = [1, 2, 3, 4]
    print(s.numTeams(rating))
