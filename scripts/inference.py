import torch
import torchaudio
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import argparse

def load_fine_tuned_model(model_path, processor_path):
    """Load fine-tuned Speech Recognition AI model and processor"""
    print(f"Loading fine-tuned Speech Recognition AI model from {model_path}")
    model = WhisperForConditionalGeneration.from_pretrained(model_path)
    processor = WhisperProcessor.from_pretrained(processor_path)
    return model, processor

def transcribe_audio(model, processor, audio_path):
    """Transcribe audio using fine-tuned Speech Recognition AI"""
    print(f"Transcribing audio file: {audio_path}")
    # Load and preprocess audio
    waveform, sample_rate = torchaudio.load(audio_path)
    inputs = processor(waveform, sampling_rate=sample_rate, return_tensors="pt")
    
    # Generate transcription using fine-tuned model
    with torch.no_grad():
        generated_ids = model.generate(inputs.input_values)
    
    # Decode transcription
    transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return transcription

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speech Recognition AI Fine Tune Inference")
    parser.add_argument("--model_path", required=True, help="Path to fine-tuned model")
    parser.add_argument("--processor_path", required=True, help="Path to fine-tuned processor")
    parser.add_argument("--audio_path", required=True, help="Path to audio file to transcribe")
    
    args = parser.parse_args()
    
    # Load fine-tuned model and processor
    model, processor = load_fine_tuned_model(args.model_path, args.processor_path)
    
    # Transcribe audio
    transcription = transcribe_audio(model, processor, args.audio_path)
    print("\nTranscription Result:")
    print(transcription)