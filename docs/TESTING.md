## Testing and Verification

### File Check

```bash
ls -l
# Expected: main.py, harpertoken/, tests/, scripts/, docs/, requirements.txt, README.md, LICENSE, .gitignore, Dockerfile, .github/
```

### Core Tests

```bash
# activate virtual environment
source venv/bin/activate

# Run all tests
# Note: In CI, transcription is skipped automatically (CI=="true").
# Locally, you'll be prompted; press 'y' to run the transcription test.
python run_tests.py

# Force run transcription via environment (non-interactive)
CI=false python run_tests.py

# Manual transcription test (requires audio input)
python tests/test_transcription.py --model_type whisper

# Verify model creation
python -c "from harpertoken.model import SpeechModel; SpeechModel('whisper'); print('Model OK')"

# Verify dataset
python -c "from harpertoken.dataset import LiveSpeechDataset; ds = LiveSpeechDataset(); print('Dataset OK')"
```

### Integration Tests

```bash
# activate virtual environment
source venv/bin/activate

# Full transcription test
python tests/test_transcription.py --model_type whisper
```

### Environment Checks

```bash
# activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Lint and format check
ruff check .
ruff format --check .

# Import validation
python -c "import harpertoken.dataset; import harpertoken.model; import harpertoken.train; print('Imports OK')"
```

### Pre-Push Hook

To prevent pushing code with linting issues, set up the pre-push hook:

```bash
cp scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

This will run `ruff check .` and `ruff format --check .` before each push and abort if there are linting or formatting issues.

Note: The pre-push hook runs during the push operation, not during commit. Since the code passed the Ruff checks (no linting or formatting issues), the hook allowed the push to proceed. If there were issues, it would have aborted the push with an error message.

The pre-push hook is a script in the repo that users need to install locally to .git/hooks/pre-push for it to run before pushes. Since it's not installed in the repo's .git/hooks (as hooks are local), it didn't run during our push. CI will still catch issues, but for local enforcement, developers should run the above commands to enable it.

### Commit Message Hook (with Ruff checks)

Install the commit message hook locally to enforce commit message policy and run Ruff on each commit:

```bash
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

Notes:
- The hook prefers `venv/bin/ruff` and falls back to `ruff` on PATH.
- Hooks are local to your clone; share the script via `scripts/` and have each collaborator install it.

### CI/CD

Tests run automatically on GitHub Actions for Python 3.8-3.12 on push/PR.

Docker image is built and pushed to GitHub Container Registry.

### OS matrix and Docker

- CI runs on an OS matrix: `ubuntu-latest`, `windows-latest`, `macos-latest`.
- Docker build and push occur only on `ubuntu-latest` (Linux runners support Docker).
- On Windows/macOS jobs, unit tests run without Docker.

Local notes by OS:
- Linux (recommended for Docker):
  - Build: `docker build -t benchmark .`
  - Run: `docker run --rm benchmark`
- macOS:
  - Ensure Docker Desktop is running to use Docker; otherwise run Python tests via venv.
- Windows:
  - Use WSL2 + Docker Desktop for Docker workflows, or run Python tests via venv.

Note: Validate workflow YAML locally before pushing:

```bash
pip install yamllint
yamllint .github/workflows/docker.yml
```
Resolve any reported lint errors (indentation, booleans, keys) before committing.

For a quick parse check using PyYAML:

```bash
python - <<'PY'
import yaml, pathlib
for p in [
    '.github/workflows/docker.yml',
    '.github/workflows/ci.yml',
    '.github/workflows/release.yml',
]:
    yaml.safe_load(pathlib.Path(p).read_text())
    print('OK:', p)
PY
```

### Docker Testing

```bash
# Build image
docker build -t benchmark .

# Run container
docker run benchmark
```
