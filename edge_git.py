import asyncio
import importlib
import edge_tts as et

async def et_save_to_file(text, voice="en-GB-SoniaNeural", file="test.mp3"):
    c = importlib.reload(et).Communicate(text, voice)
    await c.save(file)

if __name__ == "__main__":
    while True:
        text = input('')
        asyncio.run(et_save_to_file(text))
