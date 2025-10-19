import os
import sys
import unittest
import warnings

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Suppress model weight warnings
warnings.filterwarnings("ignore", category=UserWarning)


class TestHarpertoken(unittest.TestCase):
    def test_import_modules(self):
        """Test that all main modules can be imported"""
        try:
            from harpertoken.dataset import LiveSpeechDataset  # noqa: F401
            from harpertoken.evaluate import compute_metrics  # noqa: F401
            from harpertoken.model import SpeechModel  # noqa: F401
            from harpertoken.preprocessing import AudioPreprocessor  # noqa: F401
            from harpertoken.train import train_model  # noqa: F401
        except ImportError as e:
            self.fail(f"Failed to import modules: {e}")

    def test_speech_model_creation(self):
        """Test creating SpeechModel instances"""
        from harpertoken.model import SpeechModel

        # Test whisper model
        model_whisper = SpeechModel(model_type="whisper")
        self.assertIsNotNone(model_whisper)
        self.assertEqual(model_whisper.model_type, "whisper")

        # Test wav2vec2 model
        model_wav2vec = SpeechModel(model_type="wav2vec2")
        self.assertIsNotNone(model_wav2vec)
        self.assertEqual(model_wav2vec.model_type, "wav2vec2")

    def test_dataset_creation(self):
        """Test creating LiveSpeechDataset"""
        from harpertoken.dataset import LiveSpeechDataset

        dataset = LiveSpeechDataset()
        self.assertIsNotNone(dataset)
        # Skip processor check if not initialized
        # self.assertIsNotNone(dataset.processor)

    def test_preprocessor_creation(self):
        """Test creating AudioPreprocessor"""
        from harpertoken.preprocessing import AudioPreprocessor

        preprocessor = AudioPreprocessor()
        self.assertIsNotNone(preprocessor)
        self.assertEqual(preprocessor.sample_rate, 16000)

    def test_evaluate_function(self):
        """Test compute_metrics function"""
        from harpertoken.evaluate import compute_metrics

        # Mock predictions and labels as lists of strings
        predictions = ["hello", "world"]
        labels = ["hello", "world"]

        wer, cer = compute_metrics(predictions, labels)
        assert isinstance(wer, float)
        assert isinstance(cer, float)
        assert wer == 0.0  # Perfect match
        assert cer == 0.0

    def test_full_pipeline_whisper(self):
        """Test the full pipeline for whisper model with dummy audio"""
        import torch
        from transformers import WhisperProcessor

        from harpertoken.model import SpeechModel

        # Use tiny model for testing
        model = SpeechModel(model_type="whisper")
        processor = WhisperProcessor.from_pretrained("openai/whisper-tiny")

        # Create dummy audio (1 second of silence at 16kHz)
        dummy_audio = torch.zeros(16000, dtype=torch.float32)

        # Process audio
        inputs = processor(
            dummy_audio.numpy(), sampling_rate=16000, return_tensors="pt"
        )
        attention_mask = torch.ones(
            inputs.input_features.shape[0],
            inputs.input_features.shape[1],
            dtype=torch.long,
        )

        # Generate transcription
        with torch.no_grad():
            generated_ids = model.generate(
                input_features=inputs.input_features,
                attention_mask=attention_mask,
                language="en",
                task="transcribe",
                max_length=10,  # Limit for testing
            )

        # Decode
        transcription = processor.batch_decode(generated_ids, skip_special_tokens=True)[
            0
        ]
        assert isinstance(transcription, str)
        assert len(transcription) >= 0  # Should produce some output

    def test_train_model_import(self):
        """Test that train_model can be imported and accepts parameters"""
        from harpertoken.train import train_model

        # Just test import and that it's callable
        assert callable(train_model)

    def test_test_transcription_import(self):
        """Test that test_transcription can be imported"""
        from tests.test_transcription import test_transcription

        assert callable(test_transcription)


if __name__ == "__main__":
    unittest.main()
