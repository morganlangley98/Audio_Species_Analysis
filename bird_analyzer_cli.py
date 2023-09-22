import click
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
import csv
import os

@click.command()
@click.option('--min-conf', default=0.8, help='Minimum confidence threshold (default: 0.8)')
@click.option('--lat', default=55.3781, help='Latitude (default: 55.3781)')
@click.option('--lon', default=3.4360, help='Longitude (default: 3.4360)')
@click.argument('input_directory', type=click.Path(exists=True))
@click.argument('output_csv', type=click.Path())
def process_audio(min_conf, lat, lon, input_directory, output_csv):
    # Load and initialize the BirdNET-Analyzer models.
    analyzer = Analyzer()

    # Create a list to store all detections from each file
    all_detections = []

    # Iterate over the files in the directory.
    for filename in os.listdir(input_directory):
        if filename.endswith(".WAV"):  # Filter for WAV files
            file_path = os.path.join(input_directory, filename)

            # Create a Recording object for each file and analyze it.
            recording = Recording(analyzer, file_path, min_conf=min_conf, lat=lat, lon=lon)
            recording.analyze()

            # Append the detections for the current file to the all_detections list,
            # along with the recording ID.
            for detection in recording.detections:
                detection['recording_id'] = filename  # Add the recording ID
                all_detections.append(detection)

    # Write the detections to a CSV file.
    with open(output_csv, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['recording_id', 'common_name',
                                                  'scientific_name', 'start_time', 'end_time', 'confidence'])
        writer.writeheader()
        writer.writerows(all_detections)

    print("Output saved to", output_csv)

if __name__ == '__main__':
    process_audio()