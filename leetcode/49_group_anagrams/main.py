"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

from collections import Counter
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(N^2) in worst case that there are no anagrams
        # res = []
        # for st in strs:
        #     match = False
        #     an = Counter(st)
        #     for a in res:
        #         if an == Counter(a[0]):
        #             a.append(st)
        #             match = True
        #             break
        #     if not match:
        #         res.append([st])
        # return res


        # O(n log n) based on the sort
        # Hashmap based on the sorted string.  Anagrams will have matching sorted strings.
        seen = {}
        for st in strs:
            key = ''.join(sorted(st))
            if key in seen.keys():
                seen[key].append(st)
            else:
                seen[key] = [st]
        return [x for x in seen.values()]






if __name__ == "__main__":
    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.groupAnagrams(strs))

    strs = [""]
    print(s.groupAnagrams(strs))

    strs = ["a"]
    print(s.groupAnagrams(strs))
