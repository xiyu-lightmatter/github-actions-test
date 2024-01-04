# This script is used in a GitHub Actions workflow to list the files that have
# changed in the current commit. It is used to determine whether to run the
# tests or not.

import argparse
import os
import subprocess


def parse_args():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument("base_ref", help="The base ref to compare against.")
    return parser.parse_args()


def list_changed_files(base_ref):
    """Return a list of files that have changed between two branches."""
    # Removes the refs/ prefix from the branch names.
    cmd = ["git", "diff", "--name-only", f'origin/{base_ref}']
    output = subprocess.check_output(cmd, universal_newlines=True)
    return output.splitlines()


def main():
    """Print the changed files to stdout."""
    args = parse_args()
    changed_files = list_changed_files(args.base_ref)
    for f in changed_files:
        print(f)


if __name__ == "__main__":
    main()
