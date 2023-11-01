SPECIAL_NUMERALS = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
    4000: "MMMM",
}


def roman_numeral(n: int) -> str:
    if n >= 5000:
        raise ValueError("Roman numerals only go up to 4999")
    if n in SPECIAL_NUMERALS:
        return SPECIAL_NUMERALS[n]
    return construct_roman_numeral(n)


def construct_roman_numeral(n):
    result = ""
    while n != 0:
        highest_power_of_ten = 10 ** (len(str(n)) - 1)
        result += roman_numeral_of_leftmost_digit(n, highest_power_of_ten)
        n %= highest_power_of_ten
    return result


def roman_numeral_of_leftmost_digit(n, highest_power_of_ten):
    higher_position = get_higher_position(n)
    if higher_power_less_then_5(n):
        return roman_powers_of_10(higher_position, highest_power_of_ten)
    elif higher_power_more_then_5(n):
        return roman_powers_of_10_times_5(higher_position, highest_power_of_ten)
    else:
        return roman_numeral(higher_position)


def roman_powers_of_10(higher_position, highest_power_of_ten):
    return roman_numeral(highest_power_of_ten) * (
        higher_position // highest_power_of_ten
    )


def roman_powers_of_10_times_5(higher_position, highest_power_of_ten):
    return roman_numeral(highest_power_of_ten * 5) + roman_numeral(
        highest_power_of_ten
    ) * ((higher_position - highest_power_of_ten * 5) // highest_power_of_ten)


def higher_power_more_then_5(n):
    return str(n)[0] in ["6", "7", "8"]


def higher_power_less_then_5(n):
    return str(n)[0] in ["1", "2", "3"]


def get_higher_position(n: int) -> int:
    lower_positions = n % 10 ** (len(str(n)) - 1)
    return n - lower_positions
