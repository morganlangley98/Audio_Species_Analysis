#!/usr/bin/env python
# coding: utf-8

# https://github.com/mbsantiago/metamoth
from metamoth import parse_metadata

metadata = parse_metadata('input_file.WAV')

# List of metadata keys in the desired order
metadata_keys = [
    "duration_s", "samplerate_hz", "channels", "samples", "firmware_version",
    "datetime", "timezone", "audiomoth_id", "battery_state_v", "low_battery", "gain", "recording_state", "temperature_c", "amplitude_threshold",
    "frequency_filter", "deployment_id", "external_microphone",
    "minimum_trigger_duration_s", "frequency_trigger"
]


# Output table header
print("{:<25} {:<25}".format("AudioMoth Attributes", "Value"))
print("=" * 55)

# Iterate over the metadata keys and output values
for key in metadata_keys:
    value = getattr(metadata, key, "")
    print("{:<25} {:<25}".format(key, str(value)))




