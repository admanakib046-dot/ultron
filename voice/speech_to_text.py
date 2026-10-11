from faster_whisper import WhisperModel
import soundfile as sf
import tempfile
import os


class SpeechToText:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def convert(self, audio, sample_rate=16000):

        temp = tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        )

        temp.close()

        sf.write(
            temp.name,
            audio,
            sample_rate
        )

        segments, _ = self.model.transcribe(
            temp.name,
            language="en"
        )

        text = ""

        for segment in segments:
            text += segment.text + " "

        try:
            os.remove(temp.name)
        except PermissionError:
            pass

        return text.strip()