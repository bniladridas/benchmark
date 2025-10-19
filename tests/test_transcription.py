from harpertoken.dataset import LiveSpeechDataset
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torch
import argparse

def test_transcription(model_type='whisper'):
    # Load pretrained model for testing
    model_name = 'harpertoken/harpertokenASR'
    
    model = WhisperForConditionalGeneration.from_pretrained(model_name)
    processor = WhisperProcessor.from_pretrained(model_name)
    
    # Record new audio
    dataset = LiveSpeechDataset()
    audio = dataset.record_audio()
    
    # Process audio
    inputs = processor(
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
    transcription = processor.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]
    
    print(f'Transcription: {transcription}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_type', type=str, default='whisper',
                        help="Model type to use (whisper or wav2vec2)")
    args = parser.parse_args()
    
    test_transcription(model_type=args.model_type)
