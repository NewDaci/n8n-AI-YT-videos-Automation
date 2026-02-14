import os
import json
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

async def generate_script(topic: str):
    """Generate video script scenes based on topic using Google Gemini."""
    try:
        prompt = f"""Generate a short video script for the topic: "{topic}"
        
Return a JSON array with 3-5 short scene descriptions. Each scene should be a simple text string (30-50 words max).
Format: [{{"text": "scene 1"}}, {{"text": "scene 2"}}, ...]

Only return the JSON array, nothing else."""
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        
        # Parse the response as JSON
        script_text = response.text.strip()
        # Remove markdown code block markers if present
        if script_text.startswith("```json"):
            script_text = script_text[7:]
        if script_text.startswith("```"):
            script_text = script_text[3:]
        if script_text.endswith("```"):
            script_text = script_text[:-3]
        
        scenes = json.loads(script_text.strip())
        return scenes
    
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        # Fallback to default scenes if API fails
        return [
            {"text": f"Introduction to {topic}"},
            {"text": f"Key aspects of {topic}"},
            {"text": f"Conclusion about {topic}"}
        ]
