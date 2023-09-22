import click
import os
import csv
from batdetect2 import api, plot
import librosa
import soundfile

@click.command()
@click.option('--detection-threshold', default=0.3, help='Detection threshold (default: 0.3)')
@click.option('--time-expansion-factor', default=1, help='Time expansion factor (default: 1)')
@click.option('--max-duration', default=3, help='Maximum duration (default: 3)')
@click.argument('input_folder', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def process_audio(detection_threshold, time_expansion_factor, max_duration, input_folder, output_file):
    # Configure the run
    config = api.get_config(
        detection_threshold=detection_threshold,
        time_expansion_factor=time_expansion_factor,
        max_duration=max_duration,
    )

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


if __name__ == '__main__':
    process_audio()