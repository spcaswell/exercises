"""
Convert a non-negative integer num to its English words representation.



Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"



Constraints:

    0 <= num <= 231 - 1
"""


class Solution:
    def numberToWords(self, num: int) -> str:
        d = {0: "Zero",
             1: "One",
             2: "Two",
             3: "Three",
             4: "Four",
             5: "Five",
             6: "Six",
             7: "Seven",
             8: "Eight",
             9: "Nine",
             10: "Ten",
             11: "Eleven",
             12: "Twelve",
             13: "Thirteen",
             14: "Fourteen",
             15: "Fifteen",
             16: "Sixteen",
             17: "Seventeen",
             18: "Eighteen",
             19: "Nineteen",
             20: "Twenty",
             30: "Thirty",
             40: "Forty",
             50: "Fifty",
             60: "Sixty",
             70: "Seventy",
             80: "Eighty",
             90: "Ninety",
             }

        e = {0: "",
             1: "Thousand",
             2: "Million",
             3: "Billion"
             }

        n = str(num)
        i = len(n)
        j = 0
        res = ''
        while i > 0:
            res = f"{self.parse(n[max(0, i-3):i], d, e, j)} {res}"
            res = res.strip()
            i -= 3
            j += 1
        return res

    def parse(self, s: str, d: dict, e: dict, counter: int) -> str:
        if not s:
            return ''
        if len(s) == 3:
            if '000' in s:  # 000 skip grouping
                return ''
            if '00' in s[:2]:  # 001 -> One
                return f"{d[int(s[-1])]} {e[counter]}"
            if '00' in s[1:]:  # 100  One Hundred
                return f"{d[int(s[0])]} Hundred {e[counter]}"
            if '0' == s[0] and '0' == s[2]:  # 010 -> Ten
                return f"{d[int(s[1:])]} {e[counter]}"
            if '0' == s[0] and '1' == s[1]:  # 011 -> Eleven
                return f"{d[int(s[1:])]} {e[counter]}"
            if '0' == s[0]:  # 022 -> Twenty Two
                return f"{d[int(s[1])*10]} {d[int(s[2])]} {e[counter]}"
            if '0' == s[1]:  # 101 -> One Hundred One
                return f"{d[int(s[0])]} Hundred {d[int(s[2])]} {e[counter]}"
            if '0' == s[2]:  # 110 -> One Hundred Ten
                return f"{d[int(s[0])]} Hundred {d[int(s[1:])]} {e[counter]}"
            if '1' == s[1]:  # 111 -> One Hundred Eleven
                return f"{d[int(s[0])]} Hundred {d[int(s[1:])]} {e[counter]}"
            else:  # 123 -> One Hundred Twenty Three
                return f"{d[int(s[0])]} Hundred {d[int(s[1])*10]} {d[int(s[2])]} {e[counter]}"
        if len(s) == 2:
            if '0' == s[1]:  # 10 -> Ten
                return f"{d[int(s[0:])]} {e[counter]}"
            if '1' == s[0]:  # 11 -> Eleven
                return f"{d[int(s)]} {e[counter]}"
            else:  # 23 -> Twenty Three
                return f"{d[int(s[0])*10]} {d[int(s[1])]} {e[counter]}"
        else:  # Single digit return it's mapping
            return f"{d[int(s)]} {e[counter]}"



if __name__ == "__main__":
    s = Solution()

    num = 1
    print(s.numberToWords(num))

    num = 10
    print(s.numberToWords(num))

    num = 12
    print(s.numberToWords(num))

    num = 23
    print(s.numberToWords(num))

    num = 100
    print(s.numberToWords(num))

    num = 101
    print(s.numberToWords(num))

    num = 112
    print(s.numberToWords(num))

    num = 123
    print(s.numberToWords(num))

    num = 1000
    print(s.numberToWords(num))

    num = 1001
    print(s.numberToWords(num))

    num = 1010
    print(s.numberToWords(num))

    num = 1100
    print(s.numberToWords(num))

    num = 1101
    print(s.numberToWords(num))

    num = 1110
    print(s.numberToWords(num))

    num = 1111
    print(s.numberToWords(num))

    num = 1223
    print(s.numberToWords(num))

    num = 1023
    print(s.numberToWords(num))

    num = 1000010
    print(s.numberToWords(num))

    num = 12345
    print(s.numberToWords(num))

    num = 1234567
    print(s.numberToWords(num))

    num = 2454987111
    print(s.numberToWords(num))

    num = 2000000000
    print(s.numberToWords(num))
