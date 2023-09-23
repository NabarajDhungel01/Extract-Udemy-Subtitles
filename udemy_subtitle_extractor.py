import webvtt
import re
import datetime

# Function to convert WEBVTT to formatted text
def convert_webvtt_to_text(webvtt_file):
    # Read WEBVTT file
    captions = webvtt.read(webvtt_file)
    text = ""

    # Process each caption
    for caption in captions:
        caption_text = caption.text
        
        # Add line break after a full stop (.)
        caption_text = re.sub(r'\.', '.\n', caption_text)
        
        # Add three line breaks after five consecutive full stops
        caption_text = re.sub(r'\.{5}', '\n\n\n', caption_text)
        
        # Accumulate the formatted text
        text += caption_text + "\n"

    return text

# Input WEBVTT file path
webvtt_file = "your_file.vtt"  # Replace with the path to your WEBVTT file

# Convert and format the text
output_text = convert_webvtt_to_text(webvtt_file)

# Get the current time in 24-hour format
current_time = datetime.datetime.now().strftime("%H_%M")

# Create a dynamic output filename with timestamp
output_filename = f"result_{current_time}.txt"

# Save the formatted text to the dynamic output filename
with open(output_filename, "w", encoding="utf-8") as output_file:
    output_file.write(output_text)

# Display completion message with the filename
print(f"Conversion complete. The result has been saved to {output_filename}.")
