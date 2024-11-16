import pygame
import sys
import numpy as np
import track
from track import Track

#note properties
NOTE_COLOR = (255, 255, 255)
note_radius = 20
# note_x = track.SCREEN_WIDTH // 2
# note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second
track_x = {"LEFT":185,"DOWN":295,"UP":405,"RIGHT":515}
note_x = []
note_y = []
note_radii = []
num_notes = 2
timing = 50

def build_notes(tracks):
    for i in range(num_notes):
        note_x.append(tracks[0].x + 50)
        note_y.append(0-i*timing)
        note_radii.append(note_radius)

def update_note_position(i, dt):
    note_y[i] += note_speed * dt

def draw_note(i, screen):
    pygame.draw.circle(screen, NOTE_COLOR, (int(note_x[i]), int(note_y[i])), note_radius)

def reset_note(i):
    note_y[i] = -note_radii[i]

def get_y(i):
    return note_y[i]

def is_in_score_zone(i):
        if track.hit_zone_y - note_radius <= note_y[i] <= track.hit_zone_y + track.hit_zone_height:
            return True
        else:
            return False

class Note:
    def __init__(self, Track): # include track here for the track it is on
        self.NOTE_COLOR = NOTE_COLOR
        self.note_radius = note_radius
        self.note_x = Track.x + 50 # should be changed to center of the track it is initialized on
        self.note_y = note_y
        self.note_speed = note_speed
        self.track = track #left, right, up, down
        print(Track.x)

    

    



    
            
    def calculate_score(self):
        max_score = 100
        distance = abs(self.note_y-track.hit_zone_y)
        score = max_score*2.7**(-distance)

if __name__ == "__main__":
    tracks = track.build_tracks()
    note_x, note_y = build_notes(tracks)
    print(note_x[0])
    print(note_y[1])
    print(note_x[i] for i in range(num_notes))
    print(note_y[i] for i in range(num_notes))