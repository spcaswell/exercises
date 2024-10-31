"""
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

    0 <= s.length <= 1000
    s may consist of printable ASCII characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring("zxyzxyz"))
    print(s.lengthOfLongestSubstring("xxxx"))
    print(s.lengthOfLongestSubstring("pwwkew"))

