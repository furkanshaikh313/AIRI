from bardapi import Bard
import pytchat
from pytchat import LiveChat, SpeedCalculator
import time
import threading
import queue
import subprocess

# Your existing code...

# Define a queue for the worker functions to communicate
response_queue = queue.Queue()

# Define mode control variable
current_mode = "default"

# Worker function for processing messages
def process_message(message):
    global current_mode

    if current_mode == "sing":
        sing(message)
    elif current_mode == "draw":
        draw(message)
    else:
        LLM(message)

# Worker function to process responses


def draw(message):
    from gradio_client import Client

    client = Client("https://cliphamper-stabilityai-stable-diffusion-2.hf.space/")
    result = client.predict(
				message,	# str in 'Input' Textbox component
				api_name="/predict"
        )
    print(result)

def process_response(response):
    global current_mode
    if current_mode == "draw":
        edge_playback(response)
    else:
        edge_playback(response)

# Function to read chat in a separate thread
def read_chat_thread():
    video_id = input('')
    chat = pytchat.create(video_id=video_id)
    schat = pytchat.create(video_id=video_id, processor=SpeedCalculator(capacity=20))

    while chat.is_alive():
        for c in chat.get().sync_items():
            message = c.author.name + c.message

            if 'Mai' in message:
                response = LLM(message)
                response_queue.put(response)
            elif 'Meux' in message:
                search(message)
            elif 'watch' in message:
                response = sing(message)
                response_queue.put(response)
            elif 'draw' in message:
                response = draw(message)
                response_queue.put(response)

            if schat.get() >= 20:
                chat.terminate()
                schat.terminate()
                return

            time.sleep(1)
def sing(message):
    from gradio_client import Client
    messages = 'https://www.youtube.com/'
    inputs = message  + messages
    client = Client("https://2f2ccd186c3eff9b46.gradio.live")
    result = client.predict(
			inputs,	# str in 'YouTube link' Textbox component
			"Karenina",	# str (Option from: []) in 'Voice Models' Dropdown component
			0,	# int | float (numeric value between -12 and 12) in 'Pitch' Slider component
			fn_index=2
)
    print(result)


def search(message):
    output = Bard.get_answer(message)['content']
    print(output)
    edge_playback(output)



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

# Worker function to process responses
def response_worker():
    while True:
        response = response_queue.get()
        process_response(response)

# Start the threads
chat_thread = threading.Thread(target=read_chat_thread)
chat_thread.start()

response_thread = threading.Thread(target=response_worker)
response_thread.start()

# Your existing code...

# Implement mode controls
def change_mode(new_mode):
    global current_mode
    current_mode = new_mode
    print("Mode changed to:", current_mode)

# User input loop
while True:
    user_input = input("Enter mode ('sing', 'draw', or 'default'): ")
    if user_input == "exit":
        break
    if user_input in ['sing', 'draw', 'default']:
        change_mode(user_input)
