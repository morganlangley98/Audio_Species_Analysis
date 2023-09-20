# Audio_Species_Analysis
This is a user friendly guide to analysing wav. audio files for bird and bat species diversity in Jupyter notebooks.

With the rise in easily accessable recording devices, I thought it would be great to have an easy option available for less-code minded people to analyse their files for species. If you are interested in monitoring for birds and bats yourself, I would reccomend using an AudioMoth https://www.openacousticdevices.info/audiomoth.

I did not create the models, only wrote the code for implementation.

# BirdNET
The Jupyter notebooks implementation will analyse your file of audio clips and produce a CSV file of the Bird species with the "recording_id", "common_name", "scientific_name", "start_time", "end_time" and "confidence" as columns. 


All code relating to the model and downloading the required packages can be found here https://github.com/kahst/BirdNET-Analyzer/blob/main/README.md.

# BatDetect2
The Jupyter notebooks implementation will analyse your file of audio clips and produce a CSV file of the Bat species with the "recording_id", "start_time", "end_time", "low_freq", "high_freq", "class", "class_prob" and "det_prob" as columns.


All code relating to the model and downloading the required packages can be found here https://github.com/macaodha/batdetect2/blob/main/batdetect2_notebook.ipynb.

# MetaMoth
This is a great package that unlockes the associated meta data with each audio moth file. https://github.com/mbsantiago/metamoth
