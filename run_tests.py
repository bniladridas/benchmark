#!/usr/bin/env python3
"""
Script to run all tests for the harpertoken project.
"""

import os
import subprocess
import sys


def run_command(cmd, timeout=None):
    """Run command with venv activated"""
    # Resolve project directory robustly even if __file__ is empty
    project_dir = os.path.abspath(os.path.dirname(__file__) or os.getcwd())

    # Prefer the repository venv python, but fall back safely
    venv_bin = os.path.join(project_dir, "venv", "bin")
    candidate_python = os.path.join(venv_bin, "python3")
    if not os.path.exists(candidate_python):
        candidate_python = sys.executable or "python3"

    env = os.environ.copy()
    env["PYTHONPATH"] = project_dir

    full_cmd = [candidate_python] + cmd
    result = subprocess.run(
        full_cmd,
        check=False,
        cwd=project_dir,
        capture_output=True,
        text=True,
        env=env,
        timeout=timeout,
    )
    return result


def run_unit_tests():
    """Run unit tests"""
    print("Running unit tests...")
    result = run_command(["-m", "unittest", "tests.test_unit"], timeout=60)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    return result.returncode == 0


def run_transcription_test():
    """Run transcription test (requires audio input)"""
    print("Running transcription test (this will attempt to record audio)...")
    result = run_command(
        ["-u", "tests/test_transcription.py", "--model_type", "whisper"],
        timeout=60,
    )
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    return result.returncode == 0


def main():
    print("Starting all tests for harpertoken...")

    # Run unit tests
    unit_success = run_unit_tests()
    print(f"Unit tests: {'PASSED' if unit_success else 'FAILED'}")

    # Optionally run transcription test
    if os.environ.get("CI") == "true":
        run_e2e = "n"  # Skip in CI
    else:
        try:
            run_e2e = (
                input(
                    "Run transcription test? (requires audio input, may hang) [y/N]: ",
                )
                .lower()
                .strip()
            )
        except EOFError:
            run_e2e = "n"
    if run_e2e == "y":
        trans_success = run_transcription_test()
        print(f"Transcription test: {'PASSED' if trans_success else 'FAILED'}")
    else:
        trans_success = True  # Skip
        print("Transcription test: SKIPPED")

    if unit_success and trans_success:
        print("All tests passed!")
        return 0
    print("Some tests failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
