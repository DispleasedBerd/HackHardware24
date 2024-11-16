import pygame
import sys
import track

#note properties
NOTE_COLOR = (255, 255, 255)
note_radius = 20
note_x = track.SCREEN_WIDTH // 2
note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second

def create_note():
    global note_y
    note_y = 0

def reset_note():
    global note_y
    note_y = -note_radius

def draw_note():
    pygame.draw.circle(track.screen, NOTE_COLOR, (note_x, int(note_y)), note_radius)

def update_note_position(dt):
    global note_y
    note_y += note_speed * dt
