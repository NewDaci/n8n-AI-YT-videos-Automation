from pipeline.script import generate_script
from pipeline.voice import generate_voice
from pipeline.visuals import fetch_visuals
from pipeline.video import build_video

async def generate_video(topic: str):

    print("Starting video generation....")
    script = await generate_script(topic)
    print("Successfully generated script for topic:", topic)

    print("Generating voiceover...")
    audio_files = await generate_voice(script)
    print("Successfully generated audio files!")

    print("Fetching visuals...")
    visuals = await fetch_visuals(script)
    print("Successfully fetched visuals!")

    output_path = await build_video(script, audio_files, visuals)
    # output_path = "outputs/final.mp4" 

    return {
        "status": "success",
        "video": output_path
    }
