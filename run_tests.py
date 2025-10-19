#!/usr/bin/env python3
"""
Script to run all tests for the harpertoken project.
"""

import subprocess
import sys
import os

def run_unit_tests():
    """Run unit tests"""
    print("Running unit tests...")
    result = subprocess.run([
        sys.executable, '-m', 'unittest', 'tests.test_unit'
    ], cwd=os.path.dirname(__file__), capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    return result.returncode == 0

def run_transcription_test():
    """Run transcription test (requires audio input)"""
    print("Running transcription test (this will attempt to record audio)...")
    result = subprocess.run([
        sys.executable, 'tests/test_transcription.py', '--model_type', 'whisper'
    ], cwd=os.path.dirname(__file__), capture_output=True, text=True, timeout=30)
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
    run_e2e = input("Run transcription test? (requires audio input, may hang) [y/N]: ").lower().strip()
    if run_e2e == 'y':
        trans_success = run_transcription_test()
        print(f"Transcription test: {'PASSED' if trans_success else 'FAILED'}")
    else:
        trans_success = True  # Skip
        print("Transcription test: SKIPPED")

    if unit_success and trans_success:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed.")
        return 1

if __name__ == '__main__':
    sys.exit(main())