import pytest

from diff_selector.main import diff_selector


@pytest.fixture
def diffs():
    return [
        {
            "type": "changed",
            "old_filename": "file",
            "new_filename": "file",
            "line_counts": {"added": 4, "deleted": 3, "same": 27},
        }
    ]

def test_rule1(diffs):
    assert diff_selector("file", diffs) == 0
