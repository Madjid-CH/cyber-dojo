#Write a program to determine if the parentheses (),
# the brackets [], and the braces {}, in a string are balanced.
#
# For example:
#
# {{)(}} is not balanced because ) comes before (
#
# ({)} is not balanced because ) is not balanced between {} and
# similarly the { is not balanced between ()
#
# [({})] is balanced
#
# {}([]) is balanced
#
# {()}[[{}]] is balanced
import pytest

from balanced_parantheses.main import is_balanced


@pytest.mark.parametrize("input,expected", [
    ("{{)(}}", False),
    ("({)}", False),
    ("[({})]", True),
    ("{}([])", True),
    ("{()}[[{}]]", True),
])
def test_is_balanced(input, expected):
    assert is_balanced(input) == expected