from voice.microphone import Microphone
from voice.speech_to_text import SpeechToText
from voice.text_to_speech import TextToSpeech
from voice.wake_word import WakeWord

from brain.thinking import Thinking


wake = WakeWord()
mic = Microphone()
stt = SpeechToText()
tts = TextToSpeech()

brain = Thinking()

print("\n========================")
print(" Ultron Voice Online ")
print("========================\n")

while True:

    audio = mic.listen()

    command = stt.convert(audio)

    if not command:
        continue

    print("\nYou:", command)

    # -------------------------
    # Global exit commands
    # -------------------------
    if command.lower().strip() in [
        "exit",
        "quit",
        "stop",
        "shutdown",
        "shut down",
        "bye",
        "goodbye",
    ]:
        tts.speak("Goodbye.")
        break

    # -------------------------
    # Wake word detection
    # -------------------------
    if not wake.detected(command):
        continue

    # Remove wake word
    clean_command = wake.remove(command)

    # If user only says the wake word
    if clean_command == "":
        tts.speak("Yes?")
        continue

    # Stop after wake word
    if clean_command.lower() in [
        "exit",
        "quit",
        "stop",
        "shutdown",
        "shut down",
        "bye",
        "goodbye",
        "sleep",
    ]:
        tts.speak("Goodbye.")
        break

    # Process command
    answer = brain.process(clean_command)

    print("\nUltron:", answer)

    tts.speak(answer)