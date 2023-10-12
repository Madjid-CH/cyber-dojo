SPECIAL_NUMBERS = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "CM": 900,
    "D": 500,
    "M": 1000,
}

MULTIPLES_OF_9 = {"IX", "XC", "CM"}
MULTIPLES_OF_4 = {"IV", "XL", "CD"}
MULTIPLES_OF_5 = {"V", "L", "D"}
POWERS_OF_10 = {"I", "X", "C", "M"}


def reverse_roman(s: str) -> int:
    if s == "":
        return 0
    if s in SPECIAL_NUMBERS:
        return SPECIAL_NUMBERS[s]
    if s[:2] in MULTIPLES_OF_9.union(MULTIPLES_OF_4):
        return reverse_roman(s[:2]) + reverse_roman(s[2:])
    if s[0] in POWERS_OF_10.union(MULTIPLES_OF_5):
        i = get_position_number(s)
        return reverse_roman(s[0]) * (i + 1) + reverse_roman(s[i + 1:])


def get_position_number(s):
    for i in range(len(s)):
        if s[i] != s[0]:
            return i - 1
    return len(s) - 1
