"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.



Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false



Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        r = s[:]
        while True:
            if s == goal:
                return True
            else:
                t = s[0]
                s = s[1:] + t
                if s == r:
                    return False

    def rotateString_one_liner(self, s: str, goal: str) -> bool:
        """
        If s can be rotated to goal then goal must be a substring of s + s.  Also, s and goal must be of equal
        length.

        :param s:
        :param goal:
        :return:
        """
        return len(s) == len(goal) and s in goal + goal


if __name__ == "__main__":
    s = Solution()
    print(s.rotateString("abcde", "cdeab"))
    print(s.rotateString("abcde", "abced"))
