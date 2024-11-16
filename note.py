import pygame
import sys
import numpy as np
import track
from track import Track

#note properties
NOTE_COLOR = (255, 255, 255)
note_radius = 20
note_x = track.SCREEN_WIDTH // 2
note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second
track_x = {"LEFT":185,"DOWN":295,"UP":405,"RIGHT":515}
note_x = []
note_y = []
num_notes = 4
timing = 50

def build_notes(tracks):
    for i in range(num_notes):
        note_x.append(Track)
        note_y.append(0-i*timing)
    return note_x, note_y

class Note:
    def __init__(self, Track): # include track here for the track it is on
        self.NOTE_COLOR = NOTE_COLOR
        self.note_radius = note_radius
        self.note_x = Track.x + 50 # should be changed to center of the track it is initialized on
        self.note_y = note_y
        self.note_speed = note_speed
        self.track = track #left, right, up, down
        print(Track.x)

    def reset_note(self):
        self.note_y = -self.note_radius

    def draw_note(self, screen):
        pygame.draw.circle(screen, NOTE_COLOR, (self.note_x, int(self.note_y)), self.note_radius)

    def update_note_position(self, dt):
        self.note_y += self.note_speed * dt

    def is_in_score_zone(self):
        if track.hit_zone_y - self.note_radius <= self.note_y <= track.hit_zone_y + track.hit_zone_height:
            return True
        else:
            return False
            
    def calculate_score(self):
        max_score = 100
        distance = abs(self.note_y-track.hit_zone_y)
        score = max_score*2.7**(-distance)