#!/usr/bin/env python
# coding: utf-8

# In[10]:


# https://github.com/macaodha/batdetect2/blob/main/batdetect2_notebook.ipynb
from batdetect2 import api, plot
import os
import librosa
import soundfile
import csv


# In[11]:


# Configure the run
config = api.get_config(
    detection_threshold=0.3,
    time_expansion_factor=1,
    max_duration=3,
)
# Specify the input folder containing WAV files
input_folder = "input_folder"
# Specify the output CSV file path
output_file = "ouput_file.csv"
# Initialize an empty list to store the results
all_results = []
# Process each WAV file in the input folder
for file_name in os.listdir(input_folder):
    if not file_name.endswith(".WAV"):
        continue
        
    file_path = os.path.join(input_folder, file_name)
    results = api.process_file(file_path, config=config)
    if "pred_dict" not in results:
        continue
        
    detections = results["pred_dict"]["annotation"]
    for detection in detections:
        recording_id = os.path.splitext(file_name)[0]
        all_results.append((
            recording_id,
            detection["start_time"],
            detection["end_time"],
            detection["low_freq"],
            detection["high_freq"],
            detection["class"],
            detection["class_prob"],
            detection["det_prob"],
        ))
# Save the results to a CSV file
with open(output_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
         "recording_id",
         "start_time",
         "end_time",
         "low_freq",
         "high_freq",
         "class",
         "class_prob",
         "det_prob",
    ])
    writer.writerows(all_results)
print("CSV file saved successfully.")

