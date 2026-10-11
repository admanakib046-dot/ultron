from voice.microphone import Microphone
from voice.speech_to_text import SpeechToText


mic = Microphone()

stt = SpeechToText()

audio = mic.listen()

text = stt.convert(audio)

print("\nYou said:")
print(text)