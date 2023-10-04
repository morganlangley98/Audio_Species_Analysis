#!/usr/bin/env python
# coding: utf-8

# If required
# Set up for mac
xcode-select --install
Apple silicon
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/Downloads/Miniconda3-latest-MacOSX-arm64.sh
bash ~/Downloads/Miniconda3-latest-MacOSX-arm64.sh -b -p $HOME/miniconda
# The installer prompts “Do you wish the installer to initialize Miniconda3 by running conda init?” We recommend “yes”.
conda create -n birdnet-analyzer python=3.10 -c conda-forge -y
conda activate birdnet-analyzer
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos tensorflow-metal
conda install -c conda-forge librosa resampy -y
git clone https://github.com/kahst/BirdNET-Analyzer.git
cd BirdNET-Analyzer
pip install birdnetlib

from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
import csv
import os
