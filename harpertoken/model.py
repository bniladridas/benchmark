import torch
import torch.nn as nn
from transformers import Wav2Vec2Model, WhisperForConditionalGeneration

class SpeechModel(nn.Module):
    def __init__(self, model_type='whisper'):
        super(SpeechModel, self).__init__()
        self.model_type = model_type
        
        if model_type == 'wav2vec2':
            self.model = Wav2Vec2Model.from_pretrained('facebook/wav2vec2-base-960h')
            self.fc = nn.Linear(768, 32)  # Adjust output size as needed
        elif model_type == 'whisper':
            self.model = WhisperForConditionalGeneration.from_pretrained('openai/whisper-small')
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

    def forward(self, inputs, labels=None):
        if self.model_type == 'wav2vec2':
            # Ensure proper input dimensions for Wav2Vec2
            if inputs.dim() == 4:
                inputs = inputs.squeeze(1)
            outputs = self.model(inputs).last_hidden_state
            outputs = self.fc(outputs)
            return outputs
        elif self.model_type == 'whisper':
            if labels is not None:
                return self.model(input_features=inputs, labels=labels)
            return self.model(input_features=inputs)
