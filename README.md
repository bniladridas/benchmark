## files

- harpertoken/ – core modules
- tests/ – test scripts
- scripts/ – utilities
- main.py – entry point
- requirements.txt – dependencies

## usage

```python
from harpertoken.model import SpeechModel
from harpertoken.dataset import LiveSpeechDataset
from transformers import WhisperProcessor, Wav2Vec2FeatureExtractor
import torch

# choose model type: 'whisper' or 'wav2vec2'
model_type = 'whisper'  # or 'wav2vec2'

# load a speech model
model = SpeechModel(model_type=model_type)

# load appropriate processor
if model_type == 'whisper':
    processor = WhisperProcessor.from_pretrained('openai/whisper-small')
else:
    processor = Wav2Vec2FeatureExtractor.from_pretrained('facebook/wav2vec2-base-960h')

# record or load audio
dataset = LiveSpeechDataset()
audio = dataset.record_audio()

# process audio
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")

# for whisper, add attention_mask
if model_type == 'whisper':
    attention_mask = torch.ones(inputs.input_features.shape[0], inputs.input_features.shape[1], dtype=torch.long)
    generate_kwargs = {
        'input_features': inputs.input_features,
        'attention_mask': attention_mask,
        'language': 'en',
        'task': 'transcribe'
    }
else:
    generate_kwargs = {
        'input_values': inputs.input_values
    }

# generate transcription
with torch.no_grad():
    generated_ids = model.generate(**generate_kwargs)

# decode transcription
transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f'transcription: {transcription}')
```

## training

```python
from harpertoken.train import train_model

# train the model (whisper or wav2vec2)
train_model(model_type='whisper')  # or 'wav2vec2'
```

## testing the model

see [docs/testing.md](docs/TESTING.md) for detailed testing instructions.

```bash
# activate virtual environment
source venv/bin/activate

# run all tests
./run_tests.py

# or run transcription test directly (whisper or wav2vec2)
python tests/test_transcription.py --model_type whisper  # or --model_type wav2vec2
```

```python
# or programmatically
from tests.test_transcription import test_transcription
test_transcription()  # uses default whisper
```

## docker

build the docker image:

```bash
docker build -t benchmark .
```

run the container:

```bash
docker run benchmark
```

## related models

- [harpertokenASR on Hugging Face](https://huggingface.co/harpertoken/harpertokenASR)

## versioning

this project uses [semantic versioning](https://semver.org/) with automated releases via [semantic-release](https://github.com/semantic-release/semantic-release).

versions are automatically bumped and tagged based on conventional commit messages:
- `feat:` commits trigger minor version bumps
- `fix:` commits trigger patch version bumps
- `BREAKING CHANGE` in commits trigger major version bumps

releases are created on pushes to the main branch. check the [releases page](https://github.com/bniladridas/benchmark/releases) for version history.

## ci workflow

the ci workflow runs tests on every push and pull request to the main branch using github actions.
