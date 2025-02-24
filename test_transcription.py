from dataset import LiveSpeechDataset
from transformers import WhisperForConditionalGeneration
import torch

def test_transcription():
    # Load fine-tuned model
    model = WhisperForConditionalGeneration.from_pretrained(
        'models/speech_recognition_ai_fine_tune_20250224_233946'
    )
    
    # Record new audio
    dataset = LiveSpeechDataset()
    audio = dataset.record_audio()
    
    # Process audio
    inputs = dataset.processor(
        audio,
        sampling_rate=16000,
        return_tensors="pt"
    )
    
    # Generate transcription
    with torch.no_grad():
        generated_ids = model.generate(
            input_features=inputs.input_features
        )
    
    # Decode transcription
    transcription = dataset.processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]
    
    print(f'Transcription: {transcription}')

if __name__ == "__main__":
    test_transcription()
