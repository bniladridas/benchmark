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

# Run all tests (unit tests only in CI)
python run_tests.py

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

This will run `ruff check .` before each push and abort if there are issues.

### CI/CD

Tests run automatically on GitHub Actions for Python 3.8-3.12 on push/PR.

Docker image is built and pushed to GitHub Container Registry.

### Docker Testing

```bash
# Build image
docker build -t benchmark .

# Run container
docker run benchmark
```
