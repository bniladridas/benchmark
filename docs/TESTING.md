## Testing and Verification

### File Check

```bash
ls -l
# Expected: main.py, train.py, test_transcription.py, dataset.py, model.py, requirements.txt
```

### Core Tests

```bash
# main.py – verify model type
python main.py --model_type whisper
python main.py --model_type wav2vec2

# train.py – verify training start
python -c "from train import train_model; train_model('whisper')"

# test_transcription.py – verify transcription
python test_transcription.py --model_type whisper

# dataset.py – verify audio recording
python -c "from dataset import LiveSpeechDataset; LiveSpeechDataset().record_audio()"

# model.py – verify model load
python -c "from model import SpeechModel; SpeechModel('whisper')"
```

### Integration Tests

```bash
# Full training
python main.py --model_type whisper

# Full transcription
python test_transcription.py --model_type whisper
```

### Environment Checks

```bash
# Dependencies
pip install -r requirements.txt

# Lint check
flake8 .

# Import validation
python -c "from dataset import LiveSpeechDataset; from train import train_model; from test_transcription import test_transcription; print('Imports OK')"
```
