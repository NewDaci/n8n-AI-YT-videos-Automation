from fastapi import FastAPI
from pydantic import BaseModel
from pipeline.runner import generate_video
from fastapi.responses import FileResponse

app = FastAPI()

class TopicInput(BaseModel):
    topic: str

# @app.post("/generate-video")
# async def create_video(data: TopicInput):
#     result = await generate_video(data.topic)
#     return result

@app.post("/generate-video")
async def create_video(data: TopicInput):
    result = await generate_video(data.topic)

    video_path = result["video"]

    return FileResponse(
        path=video_path,
        media_type="video/mp4",
        filename="outputs/final.mp4"
    )