import argparse
from train import train_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_type', type=str, default='whisper',
                       help="Model type to use (whisper or wav2vec2)")
    args = parser.parse_args()
    
    train_model(model_type=args.model_type)
