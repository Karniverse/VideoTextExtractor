import cv2
import pytesseract
import csv

# Set the path to the Tesseract executable (change it based on your installation)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get the location of the video from user input
video_path = input(r'Enter the location of the video: ').replace("\"", "")
print(f"Starting to process: {video_path}")
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Create a CSV file to write the extracted text
csv_file_path = 'extracted_text.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header to the CSV file
    csv_writer.writerow(['Frame Number', 'Extracted Text'])

    # Loop through each frame of the video
    frame_number = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if the video has ended
        if not ret:
            break

        # Convert the frame to grayscale for better OCR results
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform OCR using Tesseract
        text = pytesseract.image_to_string(gray)

        # Write the frame number and extracted text to the CSV file
        csv_writer.writerow([frame_number, text])

        # Print the extracted text
        print(f"Frame {frame_number}: {text}")

        # Increment the frame number
        frame_number += 1

# Release the video capture object
cap.release()

print(f"Extracted text has been saved to {csv_file_path}")
