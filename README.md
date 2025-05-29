![Model](https://img.shields.io/badge/Model-Fine--tuned%20Whisper%20+%20Wav2Vec2-blue)
![Size](https://img.shields.io/badge/Size-242M-blue)
![Tensor](https://img.shields.io/badge/Tensor-F32-green)

# Hear the world. Transcribe it instantly.

Effortlessly transform live audio into text with our fine-tuned Whisper and Wav2Vec2 models. Built for real-time speech recognition, this project brings low-latency transcription to life—perfect for conversations, streaming, or any dynamic audio environment.

## Powerful. Simple. Yours.
- Capture live 16kHz mono audio with ease.
- Fine-tune models in real time for unmatched accuracy.
- Switch seamlessly between Whisper and Wav2Vec2.
- Save and load models effortlessly with timestamped precision.
- English transcription, optimized for clarity.

## Get Started
Clone the repository and set up in minutes:
```bash
git clone https://github.com/bniladridas/speech-model.git
cd speech-model
pip install -r requirements.txt
```

For Linux, install audio dependencies:
```bash
sudo apt-get install libsndfile1
```

## Bring Your Voice to Life
**Fine-Tune Models**  
Train on live audio with a single command:
```bash
python main.py --model whisper
# or
python main.py --model wav2vec2
```
Press Ctrl+C to save your fine-tuned model automatically.

**Transcribe Audio**  
Test your model with real-time transcription:
```bash
python test_transcription.py --model whisper
# or
python test_transcription.py --model wav2vec2
```
Records 5 seconds of audio (customizable) and delivers instant text.

**Save Your Work**  
Models are saved to:  
`models/speech_recognition_ai_fine_tune_[model]_[timestamp]`  
Customize the path:
```bash
export MODEL_SAVE_PATH="/your/path"
python main.py --model [whisper|wav2vec2]
```

## What You Need
- Python 3.8+
- PyTorch (2.0.1 recommended)
- Transformers (4.35.0 recommended)
- Sounddevice (0.4.6)
- Torchaudio (2.0.1)  
A GPU accelerates fine-tuning. Full requirements in `requirements.txt`.

## Behind the Magic
- **Task**: Automatic Speech Recognition (ASR)
- **Models**:  
  - Whisper (`openai/whisper-small`)  
  - Wav2Vec2 (`facebook/wav2vec2-base-960h`)
- **Fine-Tuning**: Optimized on live 16kHz mono audio with Adam optimizer (learning rate 1e-5).
- **Input**: 16kHz mono audio
- **Output**: Precise English transcription

Load models from Hugging Face:
```python
from transformers import WhisperForConditionalGeneration, WhisperProcessor
model = WhisperForConditionalGeneration.from_pretrained("bniladridas/speech-recognition-ai-fine-tune")
processor = WhisperProcessor.from_pretrained("bniladridas/speech-recognition-ai-fine-tune")
```

## Project Structure
- `dataset.py`: Audio recording and preprocessing
- `train.py`: Training pipeline
- `test_transcription.py`: Real-time transcription
- `main.py`: Core fine-tuning script
- `requirements.txt`: Dependencies
- `README.md`: This guide

## Troubleshooting
**Git Push Issues**  
For non-fast-forward errors:
```bash
git pull origin main --rebase
git push origin main
```

**Stuck Processes**  
Find and stop processes:
```bash
ps aux | grep python
kill -9 <PID>
```

**Large Files**  
Exclude models from Git:
```bash
echo "models/" >> .gitignore
git add .gitignore
git rm -r --cached models/
git commit -m "Update .gitignore"
```

## Your Data, Your Models
No pre-existing dataset needed. Your live audio recordings fuel the fine-tuning process, making every model uniquely yours.

## Join the Journey
Licensed under the MIT License. Contribute, refine, and share on [GitHub](https://github.com/bniladridas/speech-model).
