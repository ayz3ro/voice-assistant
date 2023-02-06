import json

import pyaudio
from vosk import KaldiRecognizer, Model

model = Model(r"PATH")  # There write path to model
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8000
)
stream.start_stream()


def speach():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data) and (len(data) > 0)):
            speach = json.loads(rec.Result())
            if speach['text']:
                return speach['text']
