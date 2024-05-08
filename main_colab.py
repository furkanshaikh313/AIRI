import sys
import wave
from pathlib import Path
from time import sleep, time
from os import getenv
from urllib.parse import urlencode

import sounddevice as sd
import requests
import soundfile as sf
from dotenv import load_dotenv


# load environment variables
load_dotenv()
COLAB_URL = getenv('COLAB_URL')
MODEL_NAME = getenv('MODEL_NAME')
if MODEL_NAME.endswith('.pth'):
    MODEL_NAME = MODEL_NAME[:-4]
PITCH_CHANGE = int(getenv('PITCH_CHANGE'))
VOLUME_ENVELOPE = float(getenv('VOLUME_ENVELOPE'))
INDEX_RATE = float(getenv('INDEX_RATE')) if getenv('INDEX_RATE') else 0
PITCH_EXTRACTION_ALGO = getenv('PITCH_EXTRACTION_ALGO')
GPU_INDEX = getenv('GPU_INDEX')


def rvc_infer_colab():
    params_encoded = urlencode({'model': MODEL_NAME, 'pitch': PITCH_CHANGE, 'algo': PITCH_EXTRACTION_ALGO, 'volume': VOLUME_ENVELOPE, 'index_rate': INDEX_RATE})

    with open('test.mp3', 'rb') as infile:
        files = {'audio_file': infile}
        r = requests.post(f'{COLAB_URL}/infer?{params_encoded}', files=files)
    
    with open('output.mp3', 'wb') as outfile:
        outfile.write(r.content)


def play_voice():
    data, fs = sf.read('output.mp3', dtype='float32')
    sd.play(data, fs)
    sd.wait()

if __name__ == '__main__':
        rvc_infer_colab()
        play_voice()
        print("repeat")

