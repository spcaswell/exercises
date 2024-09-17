"""
Rotational Cipher
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character
 means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical
 order.

For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic
character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character
replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters
remain unchanged.

Given a string and a rotation factor, return an encrypted string.

Signature
string rotationalCipher(string input, int rotationFactor)

Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000

Output
Return the result of rotating input a number of times equal to rotationFactor.

Example 1
input = Zebra-493?
rotationFactor = 3
output = Cheud-726?

Example 2
input = abcdefghijklmNOPQRSTUVWXYZ0123456789
rotationFactor = 39
output = nopqrstuvwxyzABCDEFGHIJKLM9012345678
"""


def rotationalCipher(input_str, rotation_factor):
    cipher_text = []
    for x in input_str:
        i = ord(x)
        if 47 < i < 58:
            i = ((i - 48 + rotation_factor) % 10) + 48
            cipher_text.append(chr(i))
        elif 64 < i < 91:
            i = ((i - 65 + rotation_factor) % 26) + 65
            cipher_text.append(chr(i))
        elif 96 < i < 123:
            i = ((i - 97 + rotation_factor) % 26) + 97
            cipher_text.append(chr(i))
        else:
            cipher_text.append(x)

    return ''.join(cipher_text)


def wrap(operand, range):
    while operand > range:
        operand -= range
    return operand

if __name__ == "__main__":
    input = "Zebra - 493"
    rotationFactor = 3
    output = "Cheud - 726"
    print(output == rotationalCipher(input, rotationFactor))

    input = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
    rotationFactor = 39
    output = "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
    print(output == rotationalCipher(input, rotationFactor))
