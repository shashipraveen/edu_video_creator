from moviepy.editor import *
import os

def generate_video(image_folder, audio_file, output_file="final_video.mp4"):
    # Get list of slide images
    images = [img for img in os.listdir(image_folder) if img.endswith(".JPG") or img.endswith(".jpg")]
    images.sort()  # Ensure they're in order like Slide1.JPG, Slide2.JPG...

    if not images:
        print("❌ No images found in the folder.")
        return

    # Load audio and calculate duration per slide
    audio_clip = AudioFileClip(audio_file)
    duration_per_slide = audio_clip.duration / len(images)

    # Create video clips for each image
    clips = []
    for img in images:
        image_path = os.path.join(image_folder, img)
        clip = ImageClip(image_path).set_duration(duration_per_slide)
        clips.append(clip)

    # Combine all clips into one video
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio_clip)

    # Export final video
    video.write_videofile(output_file, fps=24)

    print(f"✅ Video created successfully: {output_file}")

# Example usage
if __name__ == "__main__":
    generate_video(image_folder="ppt_images", audio_file="output_audio.mp3")
