real-time asr using fine-tuned whisper and wav2vec2.

## usage

```python
from harpertoken.model import SpeechModel

# load a speech model
model = SpeechModel(model_type='whisper')

# for training
from harpertoken.train import train_model
train_model(model_type='whisper')

# for transcription
from tests.test_transcription import test_transcription
test_transcription()
```

## testing the model

```python
# run transcription test
python tests/test_transcription.py --model_type whisper

# or programmatically
from tests.test_transcription import test_transcription
test_transcription()
```
