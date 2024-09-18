"""
Generate all permutations of a string
"""

from itertools import permutations


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
    print('permute_called')
    if i == length:
        # print(''.join(data))
        pass
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


if __name__ == "__main__":
    string = "cat"
    n = len(string)
    data = list(string)
    permute(data, 0, n)

    print(one_liner('cat'))
