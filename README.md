# Speech Recognition Model – Operational Information

Provides real-time ASR using fine-tuned Whisper and Wav2Vec2 models.

## Features
- 16kHz mono audio input
- Real-time transcription and fine-tuning
- Supports Whisper (`openai/whisper-small`) and Wav2Vec2 (`facebook/wav2vec2-base-960h`)
- English-language transcription

## Requirements
- Python ≥ 3.8
- PyTorch ≥ 2.0.1, Transformers ≥ 4.35.0, Torchaudio ≥ 2.0.1, Sounddevice ≥ 0.4.6
- GPU optional

## Operation

### Fine-tuning
```bash
python main.py --model whisper
python main.py --model wav2vec2
````

Models are saved to:
`models/speech_recognition_ai_fine_tune_[model]_[timestamp]`

### Transcription

```bash
python test_transcription.py --model whisper
python test_transcription.py --model wav2vec2
```

Captures ~5 seconds of audio by default.

## File Summary

* `src/` – Dataset, training, model, preprocessing, evaluation
* `tests/test_transcription.py` – Real-time transcription
* `scripts/inference.py` – Audio file transcription
* `scripts/commit-msg` – Commit validation hook
* `main.py` – Entry point

## Commit Standards

Commit messages follow the format:

```
type: description
```

Examples:

* feat: add new transcription feature
* fix: resolve audio input bug
