"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.



Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'.

"""

"""
We only care about 'b' characters.  Traverse the string and count them and if we encounter an 'a' choose the minimum of 
deleting the 'a', which is tracked by current minmum deletions + 1, or by deleting all the b's we've found. 
"""

class Solution:
    def minimumDeletions(self, s: str) -> int:
        minimum_deletions = 0
        num_b = 0
        for i in s:
            if i == 'b':
                num_b += 1
            else:
                minimum_deletions = min(minimum_deletions+1, num_b)

        return minimum_deletions


if __name__ == "__main__":
    s = Solution()

    st = "aababbab"
    print(s.minimumDeletions(st))

    st = "bbaaaaabb"
    print(s.minimumDeletions(st))
