# This script is used in a GitHub Actions workflow to list the files that have
# changed in the current commit. It is used to determine whether to run the
# tests or not.

import os
import sys
import subprocess


def list_changed_files(to_branch):
    """List the files that have changed between HEAD and the given branch."""
    cmd = ["git", "diff", "--name-only", "HEAD", to_branch]
    try:
      output = subprocess.check_output(cmd).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {cmd}, exiting: {e}")
        sys.exit(1)
    return output.splitlines()


def main():
    """Print the changed files to stdout."""
    to_branch = os.environ.get("GITHUB_BASE_REF")
    if not to_branch:
        print("GITHUB_BASE_REF not set, exiting")
        sys.exit(1)

    print("Changed files:")
    changed_files = list_changed_files(to_branch)
    for f in changed_files:
        print(f)


if __name__ == "__main__":
    main()
