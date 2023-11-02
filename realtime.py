import torch
import pyaudio
import numpy as np
import soundfile as sf
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from datetime import datetime

# Load the pre-trained Wav2Vec 2.0 model and tokenizer
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")

# Initialize PyAudio to capture audio from the microphone
p = pyaudio.PyAudio()

# Set audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
CHUNK = 1024

# Initialize the stream for audio input
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
)

# Record and transcribe audio continuously
try:
    print("Recording and Transcribing... (Press Ctrl+C to stop)")
    while True:
        audio_data = stream.read(CHUNK)
        audio_array = np.frombuffer(audio_data, dtype=np.int16)

        # Inference with the Wav2Vec 2.0 model
        inputs = tokenizer(audio_array, return_tensors="pt", padding="longest")
        with torch.no_grad():
            logits = model(input_values=inputs.input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.batch_decode(predicted_ids)[0]

        # Print the transcription
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] Transcription: {transcription}")

except KeyboardInterrupt:
    print("Stopped recording and transcribing.")

# Close the audio stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()
