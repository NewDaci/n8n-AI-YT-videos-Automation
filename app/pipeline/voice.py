import edge_tts
from pathlib import Path

async def generate_voice(script):
    files = []

    # ensure output directory exists
    Path("outputs").mkdir(parents=True, exist_ok=True)

    for i, scene in enumerate(script):
        path = f"outputs/audio_{i}.mp3"
        communicate = edge_tts.Communicate(scene["text"], "en-GB-SoniaNeural")
        await communicate.save(path)
        files.append(path)

    return files
