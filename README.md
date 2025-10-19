## files

- harpertoken/ – core modules
- tests/ – test scripts
- scripts/ – utilities
- main.py – entry point
- requirements.txt – dependencies

## usage

### whisper model

```python
from harpertoken.model import SpeechModel
from harpertoken.dataset import LiveSpeechDataset
from transformers import WhisperProcessor
import torch

# use tiny model for faster testing (or whisper-small for better quality)
model = SpeechModel(model_type="whisper")
processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")

dataset = LiveSpeechDataset()
audio = dataset.record_audio()

# process audio
inputs = processor(audio, sampling_rate=16000, return_tensors="pt")
attention_mask = torch.ones(
    inputs.input_features.shape[0],
    inputs.input_features.shape[1],
    dtype=torch.long,
)

# generate transcription
with torch.no_grad():
    generated_ids = model.generate(
        input_features=inputs.input_features,
        attention_mask=attention_mask,
        language="en",
        task="transcribe",
    )

# decode transcription
transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(f"transcription: {transcription}")
```

### wav2vec2 model

```python
from harpertoken.model import SpeechModel
from harpertoken.dataset import LiveSpeechDataset
from transformers import Wav2Vec2FeatureExtractor
import torch

model = SpeechModel(model_type="wav2vec2")
processor = Wav2Vec2FeatureExtractor.from_pretrained("facebook/wav2vec2-base-960h")

dataset = LiveSpeechDataset()
audio = dataset.record_audio()

inputs = processor(audio, sampling_rate=16000, return_tensors="pt")

with torch.no_grad():
    features = model(inputs.input_values)

print(features.shape)
```

## training

```python
from harpertoken.train import train_model

# train the model (whisper or wav2vec2)
train_model(model_type="whisper")  # or "wav2vec2"
```

## testing

see [docs/TESTING.md](docs/TESTING.md) for detailed testing instructions.

### quick test

```bash
# activate virtual environment
source venv/bin/activate

# run all tests
python run_tests.py

# run individual tests
python -m unittest tests.test_unit
python tests/test_transcription.py --model_type whisper
```

### programmatic testing

```python
# unit tests
from harpertoken.model import SpeechModel
from harpertoken.dataset import LiveSpeechDataset
from harpertoken.evaluate import compute_metrics

# test model creation
model = SpeechModel(model_type="whisper")
dataset = LiveSpeechDataset()

# test evaluation
predictions = ["hello", "world"]
labels = ["hello", "world"]
wer, cer = compute_metrics(predictions, labels)
print(f"wer: {wer}, cer: {cer}")

# live transcription test
from tests.test_transcription import test_transcription
test_transcription(model_type="whisper")
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

the ci workflow runs automated tests, linting, and formatting checks on every push and pull request to the main branch using github actions. it includes:

- unit tests across python 3.8-3.12
- ruff linting (including unused code detection)
- ruff formatting checks
- docker image build and test

note: local git hooks can enforce checks before commit/push; see docs/testing.md for setup.
