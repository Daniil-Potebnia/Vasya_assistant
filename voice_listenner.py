from vosk import Model, KaldiRecognizer
import pyaudio
import json
import requests

model = Model(r"D:\My studies\assistent\vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 44100)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8000
)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print(result["text"].split())
        full_text = result["text"].split()
        if "вася" in full_text:
            if "погода" in full_text:
                response = requests.get("http://127.0.0.1:3000/current-weather").json()
                print(f'Сейчас {response["temperature"]} градусов и {response["condition"]}')
            if 'доллар' in full_text:
                response = requests.get("http://127.0.0.1:3000/currency-rate").json()
                print(f'Текущий курс доллара - {round(response["dollar"])} рублей.')

stream.stop_stream()
stream.close()
p.terminate()
