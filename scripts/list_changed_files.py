# This script is used in a GitHub Actions workflow to list the files that have
# changed in the current commit. It is used to determine whether to run the
# tests or not.

import os
import sys
import subprocess


def list_changed_files(from_branch, to_branch):
    """Return a list of files that have changed between two branches."""
    cmd = ["git", "diff", "--name-only", from_branch, "--", to_branch]
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output.splitlines()


def main():
    """Print the changed files to stdout."""
    to_branch = os.environ["GITHUB_BASE_REF"]
    from_branch = os.environ["GITHUB_HEAD_REF"]
    changed_files = list_changed_files(from_branch, to_branch)
    print("Changed files:")
    for file in changed_files:
        print(file)


if __name__ == "__main__":
    main()
