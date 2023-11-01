OPENING_PARENTHESES = ["(", "{", "["]
CLOSING_PARENTHESES = [")", "}", "]"]


def is_balanced(s):
    stack = []
    for c in s:
        if c in OPENING_PARENTHESES:
            stack.append(c)
        elif c in CLOSING_PARENTHESES:
            if len(stack) == 0:
                return False
            else:
                if not is_matching(stack.pop(), c):
                    return False
    return len(stack) == 0


def is_matching(param, c):
    if param == "(" and c == ")":
        return True
    elif param == "{" and c == "}":
        return True
    elif param == "[" and c == "]":
        return True
    return False
