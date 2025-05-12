from moviepy.editor import *
import pyttsx3
import os

def text_to_speech(text, output_file, voice_choice=0):
    """
    Converts text to speech using pyttsx3 and saves it as an audio file.
    voice_choice: 0 for default voice, 1 for second available voice, etc.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_choice].id)
    engine.save_to_file(text, output_file)
    engine.runAndWait()
    print(f"Audio saved to {output_file}")

def create_video(text, output_file, audio_file):
    """
    Creates an animated educational video.
    """
    # Generate speech audio for the text
    text_to_speech(text, audio_file)

    # Create the text clip with the provided text
    text_clip = TextClip(text, fontsize=50, color='white', font="Arial", size=(1280, 720))
    text_clip = text_clip.set_position('center').set_duration(10)  # Duration of text on screen

    # Create background color (black background for simplicity)
    background = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=10)

    # Load audio file (the narration)
    audio = AudioFileClip(audio_file)

    # Combine the background and text
    video = CompositeVideoClip([background, text_clip])

    # Set the audio for the video
    video = video.set_audio(audio)

    # Write the video file to output
    video.write_videofile(output_file, fps=24)
    print(f"Video saved to {output_file}")

# Example usage
if __name__ == "__main__":
    input_text = "Atoms are the building blocks of matter. Each element has a unique atomic structure."
    output_video = "output_video.mp4"
    output_audio = "output_audio.mp3"
    
    create_video(input_text, output_video, output_audio)  # Generate video
