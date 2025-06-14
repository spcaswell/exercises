"""
Generate all permutations of a string
"""

from itertools import permutations
from typing import Set
from collections import Counter


def one_liner(s: str):
    return set([''.join(p) for p in permutations(s)])  # Use set() to remove duplicates


def permute(data, i, length):
    """
    Use Backtracking

    :param data:  The string to permute
    :param i: The character to start permuting on
    :param length: The desired length of permutations (Typically the length of the string, but hey, you do you.)
    :return:
    """
    # print('permute_called')
    if i == length:
        print(''.join(data))
        pass
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


def perm_search(s: str, b: str) -> Set[str]:
    """
    Given two strings s and b, such that len(s) <= len(b), find all permutations of s in b
    """
    left = 0
    seen = []
    perms = set()
    letter_check = Counter(s)

    end_l = len(b) - len(s)
    while left <= end_l:
        seen.clear()
        seen.append(b[left])  # Add leftmost char to seen
        right = left + 1
        while right < left + len(s):  # window extends to the length of target string
            if b[right] in s:
                if b[right] not in seen:
                    seen.append(b[right])  # only works for target strings of distinct chars; need counter to handle this properly

                    right += 1
                    if right == left + len(s):  # permutation found
                        perms.add(b[left:right])  # set handles duplicate detection for us
                        left += 1  # move left pointer right to check for new permutation starting from second char of this permutation
                        break
                else:
                    left += 1  # we've seen char b[r] too many times; move left pointer and start over
                    break
            else:
                left = right + 1  # char b[r] cannot be in a permutation so move l beyond that char and start over
                break
    return perms


def counter_perm_search(s: str, b: str) -> Set[str]:
    """
        Given two strings s and b, such that len(s) <= len(b), find all permutations of s in b
        Now with Counters!!
    """
    left = 0
    perms = set()
    letter_check = Counter(s)

    while left <= len(b) - len(s):
        right = left + len(s)
        perm_check = Counter(b[left:right])
        if perm_check == letter_check:
            perms.add(b[left:right])
        left += 1
    return perms


if __name__ == "__main__":
    string = "cat"
    n = len(string)
    data = list(string)
    permute(data, 0, n)

    print(one_liner('cat'))

    print(perm_search("cat", "catcta"))
    print(counter_perm_search("cat", "catcta"))
    print(counter_perm_search("caat", "caatcta"))

