import random
import json
import librosa 
import time

def generate_beatmap(audio_path):
    try: 
        y, sr= librosa.load(audio_path)

        #beat tracking
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

        #convert to timestamps
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)

        #generate beatmap
        beatmap = []
        for beat_time in beat_times:
            note = {
                'time': float(beat_time),
                'track': random.randint(0, 3)
            }
            beatmap.append(note)

        return beatmap
    
    except Exception as e:
        print(f"Error generating beatmap: {e}")
        return []
    
def save_beatmap_to_file(beatmap, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(beatmap, f, indent = 4)
        print(f"Beatmap saved to {filename}")
    except Exception as e:
        print(f"Error saving beatmap: {e}")

def display_beatmap(beatmap):
    print("\nGenerated Beatmap: ")
    for note in beatmap:
        print(f"Time: {note['time']:.2f}s, Track: {note['track']}")