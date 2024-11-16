import pygame
import sys
import track

#note properties
NOTE_COLOR = (255, 255, 255)
note_radius = 20
note_x = track.SCREEN_WIDTH // 2
note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second

class Note:
    def __init__(self, Track): # include track here for the track it is on
        self.NOTE_COLOR = NOTE_COLOR
        self.note_radius = note_radius
        self.note_x = Track.x + 50 # should be changed to center of the track it is initialized on
        self.note_y = note_y
        self.note_speed = note_speed
        self.track = track #left, right, up, down

    def reset_note(self):
        self.note_y = -self.note_radius

    def draw_note(self, screen):
        pygame.draw.circle(screen, self.NOTE_COLOR, (self.note_x, int(self.note_y)), self.note_radius)

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