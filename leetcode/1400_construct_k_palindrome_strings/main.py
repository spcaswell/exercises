"""
1400. Construct K Palindrome Strings

Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings
or false otherwise.


Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    1 <= k <= 105
"""

from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        letter_count = Counter(s)
        # If the k > s.length we cannot construct k strings from s and answer is false.
        if k > len(s):
            return False
        # If the number of characters that have odd counts is > k then the minimum number of palindrome strings we can construct is > k and answer is false.
        number_odd_letter_counts = 0
        for x in letter_count:
            if letter_count[x] % 2 != 0:
                number_odd_letter_counts += 1
        if number_odd_letter_counts > k:
            return False
        # Otherwise you can construct exactly k palindrome strings and answer is true.
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canConstruct(s = "leetcode", k = 3))
    print(s.canConstruct(s = "annabelle", k = 2))
    print(s.canConstruct(s="true", k = 4))