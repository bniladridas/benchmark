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
from harpertoken.models.model import CMAESAgent

# Load pretrained model
agent = CMAESAgent.from_pretrained("harpertoken/harpertoken-cartpole")

# Use for inference
action = agent.get_action(state)
# or evaluate performance
mean_reward, std_reward = agent.evaluate(num_episodes=10)
```

## Testing the Model

```python
from harpertoken.evaluation.test_model import test_model
test_model(agent, num_episodes=5)
```

## Commit Format

```
type: description
```

Examples:

* feat: add transcription feature
* fix: resolve audio input bug
