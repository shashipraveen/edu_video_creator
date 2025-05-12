from moviepy.editor import ColorClip

# Create a solid green clip of 3 seconds
clip = ColorClip(size=(640, 480), color=(0, 255, 0), duration=3)

# Save it as a video
clip.write_videofile("green_clip.mp4", fps=24)
