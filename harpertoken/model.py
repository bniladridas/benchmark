import logging
import warnings

from torch import nn
from transformers import Wav2Vec2Model, WhisperForConditionalGeneration

# Suppress model weight warnings
warnings.simplefilter("ignore", category=UserWarning)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("accelerate").setLevel(logging.ERROR)


class SpeechModel(nn.Module):
    def __init__(self, model_type="whisper"):
        super().__init__()
        self.model_type = model_type

        if model_type == "wav2vec2":
            self.model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base-960h")
            self.fc = nn.Linear(768, 32)  # Adjust output size as needed
        elif model_type == "whisper":
            self.model = WhisperForConditionalGeneration.from_pretrained(
                "openai/whisper-small",
            )
        else:
            msg = f"Unsupported model type: {model_type}"
            raise ValueError(msg)

    def forward(self, inputs, labels=None):
        if self.model_type == "wav2vec2":
            # Ensure proper input dimensions for Wav2Vec2
            if inputs.dim() == 4:
                inputs = inputs.squeeze(1)
            outputs = self.model(inputs).last_hidden_state
            outputs = self.fc(outputs)
            return outputs
        if self.model_type == "whisper":
            if labels is not None:
                return self.model(input_features=inputs, labels=labels)
            return self.model(input_features=inputs)

    def generate(self, **kwargs):
        """Generate output tokens for transcription.

        For Whisper models, this forwards directly to the underlying
        WhisperForConditionalGeneration.generate with the provided kwargs.
        """
        if self.model_type == "whisper":
            return self.model.generate(**kwargs)
        raise NotImplementedError("generate is only supported for 'whisper' in SpeechModel")
