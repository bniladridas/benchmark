Real-time ASR using fine-tuned Whisper and Wav2Vec2.

## Features

* 16kHz mono audio input
* Real-time transcription and fine-tuning
* Supports Whisper (`openai/whisper-small`) and Wav2Vec2 (`facebook/wav2vec2-base-960h`)
* English transcription

## Requirements

* Python ≥ 3.8
* PyTorch ≥ 2.0.1, Transformers ≥ 4.35.0, Torchaudio ≥ 2.0.1, Sounddevice ≥ 0.4.6

## Operation

### Fine-tuning

```bash
python main.py --model whisper
python main.py --model wav2vec2
```

Models saved to:
`models/speech_recognition_ai_fine_tune_[model]_[timestamp]`

### Transcription

```bash
python tests/test_transcription.py --model whisper
python tests/test_transcription.py --model wav2vec2
```

## Files

* `harpertoken/` – Core modules (dataset, model, training, evaluation)
* `tests/test_transcription.py` – Real-time transcription
* `scripts/inference.py` – File transcription
* `scripts/commit-msg` – Commit validator
* `main.py` – Entry point

## Usage

```python
from harpertoken.model import SpeechModel

# Load a speech model
model = SpeechModel(model_type='whisper')

# For training
from harpertoken.train import train_model
train_model(model_type='whisper')

# For transcription
from tests.test_transcription import test_transcription
test_transcription()
```

## Testing the Model

```python
# Run transcription test
python tests/test_transcription.py --model_type whisper

# Or programmatically
from tests.test_transcription import test_transcription
test_transcription()
```

## Commit Format

```
type: description
```

Examples:

* feat: add transcription feature
* fix: resolve audio input bug
