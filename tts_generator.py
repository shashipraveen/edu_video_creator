import pyttsx3
import os

def text_to_speech(text, output_filename="output_audio.wav", voice_choice=0, rate=150):
    """
    Converts text to speech using pyttsx3 and saves it as a .wav file.
    - voice_choice: index of available voices (0 = default)
    - rate: speech rate (default is 150 words per minute)
    """
    engine = pyttsx3.init()

    # Set speaking rate
    engine.setProperty('rate', rate)

    # Set voice (if multiple are available)
    voices = engine.getProperty('voices')
    if voice_choice < len(voices):
        engine.setProperty('voice', voices[voice_choice].id)
    else:
        print("⚠️ Warning: Selected voice not found, using default.")

    # Ensure output path is inside 'assets' folder
    output_path = os.path.join("assets", output_filename)

    # Save speech to file (pyttsx3 only supports .wav)
    engine.save_to_file(text, output_path)
    engine.runAndWait()

    print(f"✅ Audio saved at: {output_path}")
    return output_path

# Example usage
if __name__ == "__main__":
    input_text = "Atoms are the building blocks of matter. Each element has a unique atomic structure."
    text_to_speech(input_text, "output_audio.wav", voice_choice=0)
