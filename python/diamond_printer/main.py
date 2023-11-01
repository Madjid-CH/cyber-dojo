CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def first_line(char_index):
    return " " * char_index + "A" + " " * char_index + "\n"


def diamond_printer(char):
    char_index = CHARS.index(char)
    result = [first_line(char_index)]
    construct_top_pyramid(char_index, result)
    construct_lower_pyramid(char_index, result)
    result.insert(0, "\n")
    return "".join(result)


def construct_top_pyramid(char_index, result):
    for i in range(1, char_index + 1):
        line = " " * (char_index - i) + CHARS[i] + " " * (i * 2 - 1) + CHARS[i] + " " * (char_index - i) + "\n"
        result.append(line)


def construct_lower_pyramid(char_index, result):
    for i in range(char_index - 1, -1, -1):
        result.append(result[i])