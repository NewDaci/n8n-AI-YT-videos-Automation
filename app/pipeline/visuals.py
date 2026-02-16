import os
import requests
from pathlib import Path

# Get Pexels API key from environment
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

async def fetch_visuals(script):
    """Fetch video clips from Pexels API based on script content using HTTP requests."""
    Path("outputs").mkdir(parents=True, exist_ok=True)
    
    files = []
    
    if not PEXELS_API_KEY:
        print("Warning: PEXELS_API_KEY not set. Using fallback clips.")
        return ["outputs/clip1.mp4", "outputs/clip2.mp4"]
    
    try:
        for i, scene in enumerate(script):
            # Extract keywords from scene text (first few words)
            text = scene.get("text", "")
            keywords = " ".join(text.split()[:3])  # Use first 3 words as search query
            
            print(f"Searching Pexels for: {keywords}")
            
            # Make HTTP request to Pexels API
            url = f"https://api.pexels.com/v1/videos/search?query={keywords}&per_page=1"
            headers = {
                "Authorization": PEXELS_API_KEY
            }
            
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                data = response.json()
                
                videos = data.get("videos", [])
                if videos:
                    video_info = videos[0]
                    # Get the video file with smallest size
                    video_files = video_info.get("video_files", [])
                    if video_files:
                        video_url = video_files[0]["link"]
                        
                        # Download video
                        output_path = f"outputs/clip_{i}.mp4"
                        video_response = requests.get(video_url, stream=True)
                        
                        if video_response.status_code == 200:
                            with open(output_path, "wb") as f:
                                for chunk in video_response.iter_content(chunk_size=8192):
                                    if chunk:
                                        f.write(chunk)
                            files.append(output_path)
                            print(f"Downloaded: {output_path}")
                        else:
                            print(f"Failed to download video for scene {i}")
                    else:
                        print(f"No video files found for: {keywords}")
                else:
                    print(f"No videos found for: {keywords}")
            
            except requests.exceptions.RequestException as e:
                print(f"Error fetching video for '{keywords}': {e}")
        
        return files if files else ["outputs/clip1.mp4", "outputs/clip2.mp4"]
    
    except Exception as e:
        print(f"Error fetching visuals from Pexels: {e}")
        # Fallback to default clips
        return ["outputs/clip1.mp4", "outputs/clip2.mp4"]


