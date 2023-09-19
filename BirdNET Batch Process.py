#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import csv
import os

# Load and initialize the BirdNET-Analyzer models.
analyzer = Analyzer()

# Specify the directory containing the WAV files.
directory = "Your_audio_file_directory"

# Create a list to store all detections from each file
all_detections = []

# Iterate over the files in the directory.
for filename in os.listdir(directory):
    if filename.endswith(".WAV"):  # Filter for WAV files
        file_path = os.path.join(directory, filename)

        # Create a Recording object for each file and analyze it.
        recording = Recording(analyzer, file_path, min_conf=0.8, # Confidence threshold
                              lat=55.3781,lon=3.4360) # Change accordingly
        recording.analyze()

        # Append the detections for the current file to the all_detections list,
        # along with the recording ID.
        for detection in recording.detections:
            detection['recording_id'] = filename  # Add the recording ID
            all_detections.append(detection)

# Define the output CSV file path.
output_csv_path = "File_name.csv"

# Write the detections to a CSV file.
with open(output_csv_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['recording_id', 'common_name',
                                              'scientific_name', 'start_time', 'end_time', 'confidence'])
    writer.writeheader()
    writer.writerows(all_detections)

print("Output saved to", output_csv_path)

