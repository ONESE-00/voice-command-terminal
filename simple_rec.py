# import required libraries
import sounddevice as sd
import wavio as wv
import keyboard as kb

# Sampling frequency
freq = 44100

# Recording duration
duration = 3

#def start_recording():
    #press r to start recording 
    

# Start recorder with the given values 
# of duration and sample frequency
#recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

recording = sd.rec(int(duration * freq), freq,channels=2)
# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
#write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("recording2.wav", recording, freq, sampwidth=2)
