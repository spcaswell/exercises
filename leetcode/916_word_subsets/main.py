"""
916. Word Subsets

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

    For example, "wrr" is a subset of "warrior" but is not a subset of "world".

A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]

Constraints:

    1 <= words1.length, words2.length <= 104
    1 <= words1[i].length, words2[i].length <= 10
    words1[i] and words2[i] consist only of lowercase English letters.
    All the strings of words1 are unique.
"""


from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> list[str]:
        universal_words = []
        words2_character_frequency = Counter()
        for x in words2:
            frequency = Counter(x)
            for f in frequency:
                if f not in words2_character_frequency:
                    words2_character_frequency[f] = frequency[f]
                else:
                    if frequency[f] > words2_character_frequency[f]:
                        words2_character_frequency[f] = frequency[f]
        for y in words1:
            char_frequency = Counter(y)
            char_frequency.subtract(words2_character_frequency)
            missing = [z for z in char_frequency if char_frequency[z] < 0]
            if missing:
                continue
            else:
                universal_words.append(y)

        return universal_words



if __name__ == "__main__":
    s = Solution()
    print(s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
    print(s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))
    print(s.wordSubsets(words1=["amazon", "apple", "facebook", "google", "leetcode"], words2=["lo", "eo"]))
    print(s.wordSubsets(words1=["bcedecccdb","daeeddecbc","ecceededdc","edadadccea","ebacdedcea","eddabdacec","cddbecbeca","eeababedcc","bcaddcdbad","aeeeeabeea"], words2=["cb","aae","ccc","ab","adc"]))