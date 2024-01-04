"""Runs flake8 on the given list of files.

Using this script, we can run flake8 on only the files that have changed in the
current commit.

"""


import argparse
import os
import subprocess
import list_changed_files


def parse_args():
    """Parse command-line arguments using argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument("base_ref", help="The base ref to compare against.")
    parser.add_argument("head_ref", nargs="?", default="",
                        help="The head ref to compare against.")
    return parser.parse_args()


def run_flake8(files):
    """Run flake8 on the given list of files."""
    cmd = ["flake8"] + files
    subprocess.check_call(cmd)


def main():
    """Run flake8 on the changed files."""
    args = parse_args()
    changed_files = list_changed_files.list_changed_files(args.base_ref,
                                                          args.head_ref)
    run_flake8(changed_files)


if __name__ == "__main__":
    main()
