Video Compressor
Description
This Python application allows users to compress video files in a selected folder and its subfolders. It uses ffmpeg for video compression, providing a simple GUI to select the folder and set the compression quality.

Features
Compress all video files in a selected folder and its subfolders.
Supports .mp4, .avi, .mkv, and .mov formats.
Adjustable compression quality using CRF (Constant Rate Factor).
Multithreading to keep the GUI responsive during compression.
Real-time log display of the compression process.
Requirements
Python 3.x
ffmpeg installed and added to the system's PATH.
Installation
Ensure Python 3.x is installed on your system.
Install ffmpeg and add it to your system's PATH.
Clone this repository or download the source code.
Usage
Run the script using Python:
Copy code
python video_compressor.py
Click on "Seleccionar Carpeta" to choose the folder containing the videos.
Adjust the CRF value for desired compression quality.
Click on "Comenzar Compresión" to start the compression process.
Monitor the progress in the log area.
