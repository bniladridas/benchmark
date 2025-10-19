Real-time ASR using fine-tuned Whisper and Wav2Vec2.

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
