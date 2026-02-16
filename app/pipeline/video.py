from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

async def build_video(script, audio_files, visuals):
    clips = []

    try:
        for v, a in zip(visuals, audio_files):
            video = VideoFileClip(v)
            audio = AudioFileClip(a)
            
            if video.duration < 0.5:
                continue
            
            video = video.with_fps(24)

            # Set video clip to match audio duration
            clip = (
                video
                .with_audio(audio)
                .with_duration(audio.duration)
                .with_fps(24)
            )

            clips.append(clip)

        final = concatenate_videoclips(clips, method="compose")

        output = "outputs/final.mp4"

        final.write_videofile(
            output,
            codec="libx264",
            audio_codec="aac",
            fps=24
        )
        final.close()
        for c in clips:
            c.close()


    except Exception as e:
        print(f"Error building video: {e}")
        output = "outputs/fallback_video.mp4"

    return output
