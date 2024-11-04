"""
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.



Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".



Constraints:

    1 <= s.length <= 105
    s consists only of lowercase English letters.
"""

import re


class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        O(N) time and Space complexity
        :param s:
        :return:
        """
        i = 0
        j = 1
        res = ''
        while i < len(s):
            if j < len(s) and s[j] == s[i]:
                j += 1
            else:
                if j - i > 2:
                    res += s[i]*2
                    i = j
                    j = i + 1
                else:
                    res += s[i:j]
                    i = j
                    j = i + 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.makeFancyString("leeetcode"))
    print(s.makeFancyString("aaabaaaa"))
    print(s.makeFancyString("aab"))
    print(s.makeFancyString("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(s.makeFancyString(""))
