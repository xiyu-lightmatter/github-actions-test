# This script is used in a GitHub Actions workflow to list the files that have
# changed in the current commit. It is used to determine whether to run the
# tests or not.

import argparse
import os
import subprocess


def parse_args():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument("from_branch")
    parser.add_argument("to_branch")
    return parser.parse_args()


def list_changed_files(from_branch, to_branch):
    """Return a list of files that have changed between two branches."""
    # Removes the refs/ prefix from the branch names.
    cmd = ["git", "diff", "--name-only", from_branch.replace("refs/", ""), f'origin/{to_branch}']
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output.splitlines()


def main():
    """Print the changed files to stdout."""
    args = parse_args()
    changed_files = list_changed_files(args.from_branch, args.to_branch)
    for f in changed_files:
        print(f)


if __name__ == "__main__":
    main()
