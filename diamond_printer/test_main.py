import pytest

from diamond_printer.main import *


def exampleC():
    in_char = "C"
    out = "\n" "  A  \n" " B B \n" "C   C\n" " B B \n" "  A  \n"
    return in_char, out


def exampleE():
    in_char = "E"
    out = (
        "\n"
        "    A    \n"
        "   B B   \n"
        "  C   C  \n"
        " D     D \n"
        "E       E\n"
        " D     D \n"
        "  C   C  \n"
        "   B B   \n"
        "    A    \n"
    )
    return in_char, out


def exampleB():
    in_char = "B"
    out = "\n" " A \n" "B B\n" " A \n"
    return in_char, out


@pytest.mark.parametrize(
    "in_char, out", [("A", "\nA\n"), exampleB(), exampleC(), exampleE()]
)
def test_diamond_printer(in_char, out):
    assert diamond_printer(in_char) == out


@pytest.mark.parametrize("char_index, out", [(0, "A\n"), (1, " A \n"), (2, "  A  \n")])
def test_first_line(char_index, out):
    assert first_line(char_index) == out
