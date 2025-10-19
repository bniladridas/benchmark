#!/usr/bin/env python3
"""
Script to update version in pyproject.toml for semantic-release.
This script is called by semantic-release during the prepare phase.
"""

import sys
from pathlib import Path


def update_version_in_pyproject(version):
    """Update the version in pyproject.toml file."""
    pyproject_path = "pyproject.toml"

    if not Path(pyproject_path).exists():
        print(f"Error: {pyproject_path} not found")
        sys.exit(1)

    # Read the current content
    with Path(pyproject_path).open() as f:
        content = f.read()

    # Update the version using regex
    # This matches: version = "0.1.0" (with any version number)
    # We'll use a more specific approach by looking for the project section
    lines = content.split("\n")
    updated = False

    for i, line in enumerate(lines):
        if line.strip() == "[project]":
            # Look for version line in the next few lines
            for j in range(i + 1, min(i + 10, len(lines))):
                if lines[j].strip().startswith("version = "):
                    lines[j] = f'version = "{version}"'
                    updated = True
                    break
            break

    if not updated:
        print(
            f"Warning: No version field found in [project] section of {pyproject_path}"
        )
        sys.exit(1)

    new_content = "\n".join(lines)

    # Write the updated content back
    with Path(pyproject_path).open("w") as f:
        f.write(new_content)

    print(f"Updated version to {version} in {pyproject_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_version.py <version>")
        sys.exit(1)

    version = sys.argv[1]
    update_version_in_pyproject(version)
