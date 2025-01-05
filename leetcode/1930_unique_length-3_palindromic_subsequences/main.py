"""
1930. Unique Length-3 Palindromic Subsequences
Medium
Topics
Companies
Hint

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".



Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".

Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")



Constraints:

    3 <= s.length <= 105
    s consists of only lowercase English letters.

"""
from collections import Counter


class Solution:
    def countPalindromicSubsequence_reorder_allowed(self, s: str) -> int:
        counts = Counter(s)
        palindromes = 0
        for c in counts:
            if counts[c] == 2:
                palindromes += len(counts) - 1
            if counts[c] >= 3:
                palindromes += len(counts)
        return palindromes

    def countPalindromicSubsequence(self, s: str) -> int:
        """
        Only test letters in the string that appear at least twice; otherwise a palindrome is impossible
        """
        palindromes = 0
        counts = Counter(s)
        valid_letters = [x for x in counts.keys() if counts[x] > 1]
        for l in valid_letters:
            if l in s:
                first = s.find(l)
                last = s.rfind(l)
                counts = Counter(s[first+1:last]) # All unique letters between first and last, exclusive, are valid length 3 palindromes
                palindromes += len(counts)

        return palindromes


if __name__ == "__main__":
    s = Solution()
    print(s.countPalindromicSubsequence("aabca"))
    print(s.countPalindromicSubsequence("adc"))
    print(s.countPalindromicSubsequence("bbcbaba"))
    print(s.countPalindromicSubsequence("ckafnafqo"))


