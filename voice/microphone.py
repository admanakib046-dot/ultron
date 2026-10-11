import sounddevice as sd
import numpy as np


class Microphone:

    def __init__(self):

        self.sample_rate = 16000
        self.channels = 1

    def listen(self, duration=5):

        print("\nListening...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="float32"
        )

        sd.wait()

        return audio