# AI Video Generation Pipeline

A FastAPI-based application that automatically generates short videos from topics using AI. The pipeline generates scripts with Google Gemini, creates voiceovers with edge-tts, fetches stock footage from Pexels, and combines everything into a final video.

## Features

- **Script Generation**: Uses Google Gemini API to create engaging video scripts based on input topics
- **Voice Generation**: Converts script text to audio using Microsoft edge-tts
- **Visual Fetching**: Downloads relevant stock video clips from Pexels API based on script content
- **Video Composition**: Combines audio and video clips into a final video file using moviepy
- **REST API**: FastAPI endpoint for easy integration and video generation on demand

## Project Structure

```
internshala/
├── app/
│   ├── main.py              # FastAPI application entry point
│   └── pipeline/
│       ├── runner.py        # Main orchestrator for video generation
│       ├── script.py        # Google Gemini integration for script generation
│       ├── voice.py         # Edge-tts integration for audio generation
│       ├── visuals.py       # Pexels API integration for video clips
│       └── video.py         # MoviePy integration for video composition
├── outputs/                 # Generated videos and media files
├── pyproject.toml           # Project dependencies and configuration
└── README.md                # This file
```

## Prerequisites

- Python 3.12 or higher
- UV package manager (or pip)

## Installation

### 1. Clone and navigate to the project

```bash
cd /home/daci/vscodez/internshala
```

### 2. Create virtual environment and install dependencies

Using UV:
```bash
uv sync
```

Or using pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```bash
export GEMINI_API_KEY="your_gemini_api_key"
export PEXELS_API_KEY="your_pexels_api_key"
```

**Getting API Keys:**

- **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey) and create a free API key
- **Pexels API**: Register at [pexels.com/api](https://www.pexels.com/api/) and get your free API key

## Running the Application

### Start the FastAPI server

```bash
# Using UV
uv run uvicorn app.main:app --reload

# Using Python directly
/.venv/bin/python -m uvicorn app.main:app --reload
```

The server will start on `http://127.0.0.1:8000`

### API Endpoints

#### Generate Video
**POST** `/generate-video`

Request body:
```json
{
  "topic": "artificial intelligence in education"
}
```

Response:
```json
{
  "status": "success",
  "video": "outputs/final.mp4"
}
```

### Example Usage

```bash
curl -X POST "http://localhost:8000/generate-video" \
  -H "Content-Type: application/json" \
  -d '{"topic": "machine learning basics"}'
```

## Pipeline Workflow

1. **Script Generation** (`script.py`): 
   - Takes a topic and calls Google Gemini API
   - Returns a structured script with 3-5 scenes

2. **Voice Generation** (`voice.py`):
   - Converts each scene's text to audio using edge-tts
   - Saves MP3 files for each scene

3. **Visual Fetching** (`visuals.py`):
   - Extracts keywords from each scene
   - Searches Pexels API for matching video clips
   - Downloads video files for each scene

4. **Video Composition** (`video.py`):
   - Combines video clips with corresponding audio
   - Sets clip duration to match audio length
   - Concatenates all clips into a single video
   - Exports final video as MP4

5. **Orchestration** (`runner.py`):
   - Coordinates all pipeline stages
   - Returns the final video path

## Dependencies

- **fastapi** (>=0.129.0) - Web framework
- **uvicorn** (>=0.40.0) - ASGI server
- **google-genai** (>=0.1.0) - Google Gemini API client
- **edge-tts** (>=7.2.7) - Microsoft Text-to-Speech
- **moviepy** (>=2.2.1) - Video composition
- **requests** (>=2.32.5) - HTTP requests
- **python-dotenv** (>=1.2.1) - Environment variable management

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key for script generation | Yes |
| `PEXELS_API_KEY` | Pexels API key for video clips | Yes |

## Troubleshooting

### Missing Output Directory
The `outputs/` directory is created automatically on first run. If issues occur, create it manually:
```bash
mkdir -p outputs
```

### API Key Issues
- Ensure your `.env` file is in the project root
- Verify API keys are correct and have not expired
- Check API key permissions and rate limits

### Video Composition Errors
- Ensure ffmpeg is installed on your system:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install ffmpeg
  
  # macOS
  brew install ffmpeg
  ```

## Performance Notes

- Initial video generation takes 2-5 minutes depending on:
  - API response times (Gemini, Pexels)
  - Video clip download sizes
  - Video composition processing
- Video files are saved to `outputs/` and can be reused

## Future Enhancements (what I'd improve next)

- [ ] Batch video generation
- [ ] Custom video templates
- [ ] Background music integration
- [ ] Video thumbnail generation
- [ ] Progress tracking and webhooks
- [ ] Storage backend integration (S3, etc.)