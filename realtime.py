import pyaudio
import numpy as np
#from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from transformers import pipeline

asr = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")


# Initialize PyAudio to capture audio from the microphone
p = pyaudio.PyAudio()

# Set audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 16000
CHUNK = 512

    

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
        
        audio_array = audio_array.astype(np.float64)
        

        #verify mic is working      
        print(audio_array)
        

        # Transcribe audio using the ASR pipeline
        #transcription = asr(np.array(audio_array))['text']
        transcription = asr(audio_array)['text']
        

        # Print the transcription
        #timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"Transcription: {transcription}")

except KeyboardInterrupt:
    print("Stopped recording and transcribing.")

# Close the audio stream and PyAudio
stream.stop_stream()
stream.close()
p.terminate()

'''
1. which is the better model btwn whisper and facebook one
2. why don't is attempt to use pipelines
3. discard the ALSA warnings and evaluate script perfomance.
'''