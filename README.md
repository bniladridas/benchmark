## usage

```python
from harpertoken.model import SpeechModel
from harpertoken.dataset import LiveSpeechDataset
from transformers import WhisperProcessor
import torch

# load a speech model
model = SpeechModel(model_type='whisper')
processor = WhisperProcessor.from_pretrained('openai/whisper-small')

# record or load audio
dataset = LiveSpeechDataset()
audio = dataset.record_audio()

# process audio
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
attention_mask = torch.ones(inputs.input_features.shape[0], inputs.input_features.shape[1], dtype=torch.long)

# generate transcription
with torch.no_grad():
    generated_ids = model.generate(
        input_features=inputs.input_features,
        attention_mask=attention_mask,
        language='en',
        task='transcribe'
    )

# decode transcription
transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f'transcription: {transcription}')
```

## training

```python
from harpertoken.train import train_model

# train the model
train_model(model_type='whisper')
```

## testing the model

```python
# run transcription test
python tests/test_transcription.py --model_type whisper

# or programmatically
from tests.test_transcription import test_transcription
test_transcription()
```
