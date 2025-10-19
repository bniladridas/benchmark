import sounddevice as sd
from torch.utils.data import Dataset
from transformers import Wav2Vec2FeatureExtractor, WhisperProcessor


class LiveSpeechDataset(Dataset):
    def __init__(self, model_type="whisper", sample_rate=16000, record_seconds=5):
        """
        Args:
            model_type (str): Model type to use (whisper or wav2vec2)
            sample_rate (int): Sample rate for audio recording
            record_seconds (int): Duration of each recording in seconds
        """
        self.model_type = model_type
        self.sample_rate = sample_rate
        self.record_seconds = record_seconds

        if model_type == "whisper":
            self.processor = WhisperProcessor.from_pretrained("openai/whisper-small")
        elif model_type == "wav2vec2":
            self.processor = Wav2Vec2FeatureExtractor.from_pretrained(
                "facebook/wav2vec2-base-960h",
            )
        else:
            msg = f"Unsupported model type: {model_type}"
            raise ValueError(msg)

        self.recordings = []
        # Record initial audio to ensure data exists
        self.record_audio()

    def __len__(self):
        return len(self.recordings)

    def __getitem__(self, idx):
        # Get audio and process it
        audio = self.recordings[idx]

        if self.model_type == "whisper":
            inputs = self.processor(
                audio, sampling_rate=self.sample_rate, return_tensors="pt",
            )
            return {"input_features": inputs.input_features.squeeze(0)}
        if self.model_type == "wav2vec2":
            inputs = self.processor(
                audio, sampling_rate=self.sample_rate, return_tensors="pt", padding=True,
            )
            # Ensure proper input dimensions for Wav2Vec2
            return {"input_values": inputs.input_values.squeeze(0).unsqueeze(0)}
        return None

    def record_audio(self):
        """Record audio from the default microphone"""
        print(f"Recording for {self.record_seconds} seconds...")
        audio = sd.rec(
            int(self.record_seconds * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="float32",
        )
        sd.wait()  # Wait until recording is finished
        print("Recording complete")

        # Convert to mono and add to recordings
        audio = audio.squeeze()
        self.recordings.append(audio)
        return audio
