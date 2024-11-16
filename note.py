import pygame
import sys
import track

# Colors
NOTE_COLOR = (255, 255, 255)


#note properties
note_radius = 20
note_x = track.SCREEN_WIDTH // 2
note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second

def create_note():
    pygame.draw.circle(track.screen, NOTE_COLOR, (note_x, int(note_y)), note_radius)
