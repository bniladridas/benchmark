![Model](https://img.shields.io/badge/Model-Fine--tuned%20Whisper%20+%20Wav2Vec2-blue)
![Size](https://img.shields.io/badge/Size-242M-blue)
![Tensor](https://img.shields.io/badge/Tensor-F32-green)

# Speech Recognition Model – Operational Information

This system provides real-time automatic speech recognition (ASR) using fine-tuned **Whisper** and **Wav2Vec2** models.

## Features

* Captures 16kHz mono audio input.
* Supports fine-tuning and real-time transcription.
* Compatible with Whisper (`openai/whisper-small`) and Wav2Vec2 (`facebook/wav2vec2-base-960h`).
* English language transcription optimized for accuracy.

## System Requirements

* **Python:** 3.8 or higher
* **Libraries:** PyTorch ≥ 2.0.1, Transformers ≥ 4.35.0, Torchaudio ≥ 2.0.1, Sounddevice ≥ 0.4.6
* **Hardware:** GPU recommended for fine-tuning

## Installation

```bash
git clone https://github.com/bniladridas/speech-model.git
cd speech-model
pip install -r requirements.txt
```

For Linux systems:

```bash
sudo apt-get install libsndfile1
```

## Operation

### 1. Fine-tuning

```bash
python main.py --model whisper
# or
python main.py --model wav2vec2
```

Press **Ctrl+C** to save the current fine-tuned model.

Models are saved to:

```
models/speech_recognition_ai_fine_tune_[model]_[timestamp]
```

To set a custom save path:

```bash
export MODEL_SAVE_PATH="/your/path"
```

### 2. Transcription

```bash
python test_transcription.py --model whisper
# or
python test_transcription.py --model wav2vec2
```

Captures ~5 seconds of audio by default.

## File Overview

* `src/dataset.py` – audio recording and preprocessing
* `src/train.py` – training logic
* `src/model.py` – model definitions
* `src/evaluate.py` – evaluation metrics
* `src/preprocessing.py` – audio preprocessing utilities
* `tests/test_transcription.py` – real-time transcription script
* `scripts/inference.py` – audio file transcription
* `scripts/commit-msg` – commit message validation hook
* `scripts/rewrite_msg.sh` – history rewrite script
* `main.py` – main fine-tuning entry point
* `requirements.txt` – dependency list

## Troubleshooting

**Non-fast-forward push error:**

```bash
git pull origin main --rebase
git push origin main
```

**Terminate stuck Python processes:**

```bash
ps aux | grep python
kill -9 <PID>
```

**Exclude large model files from version control:**

```bash
echo "models/" >> .gitignore
git add .gitignore
git rm -r --cached models/
git commit -m "Update .gitignore"
```

## Commit Standards

Commit messages must follow the **conventional commit** format:

```
type: description
```

**Examples:**

* `feat: add new transcription feature`
* `fix: resolve audio input bug`

To enable message validation:

```bash
cp scripts/commit-msg .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```