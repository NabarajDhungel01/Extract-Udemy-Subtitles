# Udemy Subtitle Extractor

This repository provides a simple solution to extract and format subtitles from Udemy course videos and save them to a text file.

## How to Extract Udemy Subtitles

Follow these easy steps to extract subtitles from Udemy course videos:

1. **Select the Video**: Choose the Udemy course video from which you want to extract subtitles.

2. **Open Developer Tools**: To start, open your browser's developer tools. You can do this by pressing `F12` or right-clicking on the video and selecting "Inspect."

3. **Go to the Network Tab**: Within the developer tools, navigate to the "Network" tab.

4. **Reload the Page**: Refresh the Udemy course page to begin monitoring network requests.

5. **Enable Subtitles**: In the video player, click on the "Subtitles" button and select your desired language for subtitles.

6. **Locate the .vtt File**: Under the "Network" tab, use the filter or search functionality to find a file with the extension .vtt (e.g., "xyz123.vtt"). This file contains the subtitles.

7. **Copy Response Text**: Right-click on the .vtt file and select "Copy" to copy the response text.

8. **Paste into `your_file.vtt`**: Create a new text file named `your_file.vtt` in the same directory as your Python script. Paste the copied response text into this file.

9. **Run the Script**: Execute the provided Python script in this repository. The script will process the .vtt file and format the subtitles.

10. **View the Output**: The formatted subtitles will be saved to an output file named `result_current_date.txt` (e.g., `result_11_15.txt`). Your extracted subtitles are ready to use!

## Advanced Formatting || Convert Subtitle to Notes / Documentation

For more advanced formatting or user-friendly content, consider using a language model like ChatGPT, Bing, or Bard. Provide the following prompt to generate beautifully formatted documentation:

```
Generate user-friendly content with the following formatting:

- Use H1, H2, and H3 headings.
- Create a list structure for steps or key points.
- Avoid excessive use of bold text.
- Make the content appear like a comprehensive set of notes or a tutorial.
- Ensure the content is written in a user-friendly, non-technical language with minimal jargon, as if it were notes taken by a student.

```
If you encounter any issues or have questions, please feel free to create an issue on GitHub.
