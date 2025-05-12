import os
import comtypes.client

def convert_ppt_to_images(ppt_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize PowerPoint application
    powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
    powerpoint.Visible = 1

    # Open the presentation
    presentation = powerpoint.Presentations.Open(ppt_path, WithWindow=False)

    # Export slides as images
    presentation.SaveAs(output_folder, 17)  # 17 = ppSaveAsJPG
    presentation.Close()
    powerpoint.Quit()

    print(f"✅ Slides exported to: {output_folder}")

# Example usage
if __name__ == "__main__":
    ppt_file = os.path.abspath("output.pptx")  # Your generated ppt file
    images_output_dir = os.path.abspath("ppt_images")
    convert_ppt_to_images(ppt_file, images_output_dir)
