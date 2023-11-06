import gradio as gr 
import time
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h")

def transcribe(audio, state=""):
    time.sleep(2)
    text = pipe(audio)["text"]
    state += text + " "
    return state

gr.Interface(
    fn = transcribe,
    inputs = [gr.Audio(sources="microphone", type="filepath"), 'state'],
    outputs = ["textbox", "state"],
    live=True).launch()  