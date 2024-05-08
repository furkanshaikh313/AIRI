from bardapi import Bard
import pytchat
from pytchat import LiveChat, SpeedCalculator
import time
global response
import subprocess

video_int = input("Enter the video url: ")

video_id = video_int

token = 'ZwhHrmqXk2imv-HXOU1JANx1UOyUa-lfLSTbELkU_7SwOT1AZELlvUnGk6jmEmIhicHT_Q.'

bard = Bard(token=token)

prompt = "Remember You are a female streamer Your Name is AIRI. you will respond in a childish and " \
         "seductive manner. you will talk about the message but sometimes go on random tangents keep your reply short around 20-25 words Strictly. " \
         "you will also make fun of people.You will act as a human but keeping in mind that you are a llm " \
         "your creator is known as ClipHamper he is a programer and you have to bug him as much as possible .If you understand"\
         "reply with 'prompt has been setup'"


promptver = bard.get_answer(prompt)['content']



print("Getting youtube Comments from the live stream: ", video_id)


def readChat():
    chat = pytchat.create(video_id=video_id)
    schat = pytchat.create(video_id=video_id, processor=SpeedCalculator(capacity=20))

    while chat.is_alive():
        global wh_words  # Global declaration of wh_words
        wh_words = ['watch', 'draw', 'Mai', 'Meux']  # Define the wh_words list
        for c in chat.get().sync_items():
            print(f"\n{c.datetime} [{c.author.name}]- {c.message}\n")
            global message
            message =  c.author.name + c.message 

            
            if 'Mai' in message:  # Check if 'Mai' is in the message
                LLM(message)
                print('AI response', output)
            elif 'Meux' in message: #Response Using Bard
                search(message)
                print('AI')
            elif 'watch' in message:  # Check if 'watch' is in the message
                message = c.message
                sing(message)
                print('singing')
            elif'draw' in message:  # Check if 'draw' is in the message
                message = c.message
                draw(message)  
                print('drawing')
            elif 'eyes' in message:
                eyes()
            if schat.get() >= 20:
                chat.terminate()
                schat.terminate()
                return

            time.sleep(1)


def draw(message):
    from gradio_client import Client

    client = Client("https://cliphamper-stabilityai-stable-diffusion-2.hf.space/")
    result = client.predict(
				message,	# str in 'Input' Textbox component
				api_name="/predict"
        )
    print(result)
    from PIL import Image

# Replace 'jpg_location' with your actual variable that stores the file location
    jpg_location = result

# Open the JPG image
    image = Image.open(jpg_location)

# Display the image
    image.show()
def sing(message):
    from gradio_client import Client
    messages = 'https://www.youtube.com/'
    inputs = messages + message
    from gradio_client import Client

    client = Client("https://ede07184d9357d6cce.gradio.live/")
    result = client.predict(
				inputs,	# str in 'Song input' Textbox component
				"Lisa",	# str (Option from: []) in 'Voice Models' Dropdown component
				-24,	# int | float (numeric value between -24 and 24) in 'Pitch Change' Slider component
				True,	# bool in 'Keep intermediate files' Checkbox component
				5,	# int | float in 'parameter_46' Number component
				-20,	# int | float (numeric value between -20 and 20) in 'Main Vocals' Slider component
				-20,	# int | float (numeric value between -20 and 20) in 'Backup Vocals' Slider component
				-20,	# int | float (numeric value between -20 and 20) in 'Music' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Index Rate' Slider component
				0,	# int | float (numeric value between 0 and 7) in 'Filter radius' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'RMS mix rate' Slider component
				0,	# int | float (numeric value between 0 and 0.5) in 'Protect rate' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Room size' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Wetness level' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Dryness level' Slider component
				0,	# int | float (numeric value between 0 and 1) in 'Damping level' Slider component
				fn_index=6
    )
    print(result)
    import pygame

# Initialize the pygame mixer
    pygame.mixer.init()

# Replace 'mp3_location' with your actual variable that stores the file location
    mp3_location = result

# Load the MP3 file
    pygame.mixer.music.load(mp3_location)

# Play the MP3 file
    pygame.mixer.music.play()

# Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def search(message):
    output = bard.get_answer(message)['content']
    print(output)
    edge_playback(output)

def eyes():
    import numpy as np
    import cv2
    import pyautogui


    image = pyautogui.screenshot()

    image2 = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2BGRA)

    cv2.imwrite('image1.png',image2)
    from gradio_client import Client

    client = Client("https://cliphamper-stablediffusionapi-anything-v5.hf.space/")
    result = client.predict(
			    'image1.png',	
		    	api_name="/predict"
    )
    print(result)

    


def LLM(message):
    import requests
    input_text = message
    global ai_response
# The URL of your Node.js server
    url = "http://localhost:3000/chat"

# Send a POST request to the server with the input text
    response = requests.post(url, json={"input": input_text})

# Check if the request was successful
    if response.status_code == 200:
    # Get the AI's response from the JSON data
        ai_response = response.json().get("output")
        print("AI Response:", ai_response)
    else:
        print("Error:", response.text)
    global output
    output = ai_response
    edge_playback(output)
    return output
    





def edge_playback(output):
    text = output
    asyncio.run(et_save_to_file(text))


import asyncio
import importlib
import edge_tts as et

async def et_save_to_file(text, voice="en-GB-SoniaNeural", file="test.mp3"):
    c = importlib.reload(et).Communicate(text, voice)
    await c.save(file)


    directory_path = "E:\RVC-beta-v2-0618\AniVoiceChanger"
    file_name = "main_colab.py"
    run_code_in_directory(directory_path, file_name)
    
def run_code_in_directory(directory_path, file_name):
    command = "python {}/{}".format(directory_path, file_name)
    subprocess.call(command, shell=True)

    



while True:
        readChat()
       
        print("\n\nReset!\n\n")
        time.sleep(2)
        