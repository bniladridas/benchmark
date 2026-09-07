<p align="center">
  <img src="https://raw.githubusercontent.com/Coccinella-Labs/benchmark/main/.github/assets/thumbnail.png" alt="benchmark" width="100%">
</p>

speech model benchmark.

Compares OpenAI Whisper against Meta's Wav2Vec2 (`facebook/wav2vec2-base-960h`) for transcription quality.

## Usage

```bash
pip install -r requirements.txt
python main.py --model_type whisper    # default
python main.py --model_type wav2vec2
```

## Layout

- `harpertoken/` - training package (`train`, `dataset`, `evaluate`, `model`, `preprocessing`)
- `tests/` - transcription and unit tests (see `docs/TESTING.md`)
- `run_tests.py` - test runner (prefers `./venv/bin/python3`)
- `Dockerfile` - containerized runs

## Stack

PyTorch, Transformers, Librosa, Datasets, scikit-learn.
