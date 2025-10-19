import torchaudio
import torchaudio.transforms as T

class AudioPreprocessor:
    def __init__(self, sample_rate=16000, n_mels=64):
        self.sample_rate = sample_rate
        self.mel_transform = T.MelSpectrogram(sample_rate=sample_rate, n_mels=n_mels)
        self.normalize = T.Resample(orig_freq=sample_rate, new_freq=sample_rate)

    def process(self, waveform):
        mel_spectrogram = self.mel_transform(waveform)
        return mel_spectrogram