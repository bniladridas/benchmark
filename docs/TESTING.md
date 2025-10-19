## Testing and Verification

### File Check

```bash
ls -l
# Expected: main.py, harpertoken/, tests/, scripts/, docs/, requirements.txt, README.md, LICENSE, .gitignore
```

### Core Tests

```bash
# activate virtual environment
source venv/bin/activate

# main.py – verify model type
python main.py --model_type whisper
python main.py --model_type wav2vec2

# train.py – verify training start
python -c "from harpertoken.train import train_model; train_model('whisper')"

# test_transcription.py – verify transcription
python tests/test_transcription.py --model_type whisper

# dataset.py – verify audio recording
python -c "from harpertoken.dataset import LiveSpeechDataset; LiveSpeechDataset().record_audio()"

# model.py – verify model load
python -c "from harpertoken.model import SpeechModel; SpeechModel('whisper')"
```

### Integration Tests

```bash
# activate virtual environment
source venv/bin/activate

# Full training
python main.py --model_type whisper

# Full transcription
python tests/test_transcription.py --model_type whisper
```

### Environment Checks

```bash
# activate virtual environment
source venv/bin/activate

# Dependencies
pip install -r requirements.txt

# Lint check
flake8 .

# Import validation
python -c "from harpertoken.dataset import LiveSpeechDataset; from harpertoken.train import train_model; from tests.test_transcription import test_transcription; print('Imports OK')"
```
