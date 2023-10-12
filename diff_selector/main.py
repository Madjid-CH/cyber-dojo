TYPES = ["deleted", "created", "renamed", "unchanged", "changed"]

def diff_selector(filename, diffs):
    for i, diff in enumerate(diffs):
        if diff["old_filename"] == filename:
            return i