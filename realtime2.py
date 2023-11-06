import sounddevice as sd  # Using sounddevice for audio input (you need to install it)
from transformers import pipeline

# Create an ASR pipeline
asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

try:
    print("Recording and Transcribing... (Press Ctrl+C to stop)")
    with sd.InputStream(callback=asr, channels=2, device=None, blocksize=1024, samplerate=16000, dtype="int16") as stream:
        sd.sleep(999999)  # Keep the script running until manually interrupted

except KeyboardInterrupt:
    print("Stopped recording and transcribing.")
