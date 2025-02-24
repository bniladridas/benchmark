# Speech Recognition AI: Fine-Tuned Whisper and Wav2Vec2 for Real-Time Audio

![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)

This project fine-tunes OpenAI's Whisper (`whisper-small`) and Facebook's Wav2Vec2 (`wav2vec2-base-960h`) models for real-time speech recognition using live audio recordings. It’s designed for dynamic environments where low-latency transcription is key, such as live conversations or streaming audio.

## Model Description
This is a fine-tuned version of [OpenAI's Whisper small model](https://huggingface.co/openai/whisper-small) and [Facebook's Wav2Vec2 base model](https://huggingface.co/facebook/wav2vec2-base-960h), optimized for real-time speech-to-text transcription. The models were trained on live 16kHz mono audio recordings, improving transcription accuracy over their base versions for continuous input scenarios.

## Features
- **Real-time audio recording**: Captures live 16kHz mono audio via microphone input.
- **Continuous fine-tuning**: Updates model weights incrementally during live sessions.
- **Speech-to-text transcription**: Converts audio to text with high accuracy.
- **Model saving/loading**: Automatically saves fine-tuned models with timestamps.
- **Dual model support**: Choose between Whisper and Wav2Vec2 architectures.

*Note*: Currently supports English-only transcription.

## Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/bniladridas/speech-model.git
cd speech-model
pip install -r requirements.txt
```

Optional: Install system dependencies for Sounddevice (e.g., libsoundio on Linux):
```bash
sudo apt-get install libsndfile1
```

## Usage

### Start Fine-Tuning
Fine-tune the model on live audio:
```bash
# For Whisper model
python main.py --model_type whisper

# For Wav2Vec2 model
python main.py --model_type wav2vec2
```
Records audio in real-time and updates the model continuously. Press Ctrl+C to stop training and save the model automatically.

### Transcription
Test the fine-tuned model:
```bash
# For Whisper model
python test_transcription.py --model_type whisper

# For Wav2Vec2 model
python test_transcription.py --model_type wav2vec2
```
Records 5 seconds of audio (configurable in code) and generates a transcription.

### Model Storage
Models are saved by default to:
```
models/speech_recognition_ai_fine_tune_[model_type]_[timestamp]
```
Example: `models/speech_recognition_ai_fine_tune_whisper_20250225`

To customize the save path:
```bash
export MODEL_SAVE_PATH="/your/custom/path"
python main.py --model_type [whisper|wav2vec2]
```

## Requirements
- Python 3.8+
- PyTorch (torch==2.0.1 recommended)
- Transformers (transformers==4.35.0 recommended)
- Sounddevice (sounddevice==0.4.6)
- Torchaudio (torchaudio==2.0.1)

A GPU is recommended for faster fine-tuning. See `requirements.txt` for the full list.

## Model Details
- **Task**: Automatic Speech Recognition (ASR)
- **Base Models**:
  - Whisper: openai/whisper-small
  - Wav2Vec2: facebook/wav2vec2-base-960h
- **Fine-tuning**: Trained on live 16kHz mono audio recordings with a batch size of 8, using the Adam optimizer (learning rate 1e-5).
- **Input**: 16kHz mono audio
- **Output**: Text transcription
- **Language**: English

## Loading the Model (Hugging Face)

To load the models from Hugging Face:
```python
from transformers import WhisperForConditionalGeneration, WhisperProcessor
model = WhisperForConditionalGeneration.from_pretrained("bniladridas/speech-recognition-ai-fine-tune")
processor = WhisperProcessor.from_pretrained("bniladridas/speech-recognition-ai-fine-tune")
```

## Repository Structure

```
speech-model/
├── dataset.py              # Audio recording and preprocessing
├── train.py                # Training pipeline
├── test_transcription.py   # Transcription testing
├── main.py                 # Main script for fine-tuning
├── README.md               # This file
└── requirements.txt        # Dependencies
```

## Training Data
The models are fine-tuned on live audio recordings collected during runtime. No pre-existing dataset is required—users generate their own data via microphone input.

## Evaluation Results
Placeholder: Future updates will include WER (Word Error Rate) metrics compared to base models.

## License
Licensed under the MIT License. See the LICENSE file for details.
