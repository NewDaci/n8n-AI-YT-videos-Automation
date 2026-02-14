from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

async def build_video(script, audio_files, visuals):
    clips = []

    try:
        for v, a in zip(visuals, audio_files):
            video = VideoFileClip(v)
            audio = AudioFileClip(a)
            clip = video.with_audio(audio).with_duration(audio.duration)
            clips.append(clip)

        final = concatenate_videoclips(clips)
        output = "outputs/final.mp4"
        final.write_videofile(output)
    
    except Exception as e:
        print(f"Error building video: {e}")
        # Fallback to a default video if processing fails
        output = "outputs/fallback_video.mp4"

    return output
