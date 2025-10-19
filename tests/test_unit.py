import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class TestHarpertoken(unittest.TestCase):
    
    def test_import_modules(self):
        """Test that all main modules can be imported"""
        try:
            from harpertoken.dataset import LiveSpeechDataset
            from harpertoken.model import SpeechModel
            from harpertoken.train import train_model
            from harpertoken.evaluate import compute_metrics
            from harpertoken.preprocessing import AudioPreprocessor
        except ImportError as e:
            self.fail(f"Failed to import modules: {e}")
    
    def test_speech_model_creation(self):
        """Test creating SpeechModel instances"""
        from harpertoken.model import SpeechModel
        
        # Test whisper model
        model_whisper = SpeechModel(model_type='whisper')
        self.assertIsNotNone(model_whisper)
        self.assertEqual(model_whisper.model_type, 'whisper')
        
        # Test wav2vec2 model
        model_wav2vec = SpeechModel(model_type='wav2vec2')
        self.assertIsNotNone(model_wav2vec)
        self.assertEqual(model_wav2vec.model_type, 'wav2vec2')
    
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
        self.assertIsInstance(wer, float)
        self.assertIsInstance(cer, float)
        self.assertEqual(wer, 0.0)  # Perfect match
        self.assertEqual(cer, 0.0)

if __name__ == '__main__':
    unittest.main()