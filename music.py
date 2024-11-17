import os
import sys
import json

# Add the directory containing beatmap.py to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

import beatmap

# Path to the assets folder
assets_folder = os.path.join(current_dir, 'assets', 'audio')

# Ensure the folder exists and contains an audio file
# try:
#     # Get the list of audio files in the folder
#     audio_files = [file for file in os.listdir(assets_folder) if file.endswith(('.mp3', '.wav', '.ogg'))]

#     if not audio_files:
#         print("No audio files found in the 'assets/audio' folder.")
#     else:
#         #megalovania beatmap
#         audio_path = os.path.join(assets_folder, audio_files[0])
#         #print(f"Using audio file: {audio_path}")
#         beatmap_data = beatmap.generate_beatmap(audio_path)
#         #beatmap.save_beatmap_to_file(beatmap_data, os.path.join(assets_folder, "megalovania_beatmap.json"))

#         #skibidi beatmap
#         audio_path = os.path.join(assets_folder, audio_files[1])
#         #print(f"Using audio file: {audio_path}")
#         beatmap_data = beatmap.generate_beatmap(audio_path)
#         #beatmap.save_beatmap_to_file(beatmap_data, os.path.join(assets_folder, "skibidi_beatmap.json"))

# except Exception as e:
#     print(f"An error occurred: {e}")

def load_beatmap(beatmap_path):
    with open(beatmap_path, 'r') as f:
        return json.load(f)