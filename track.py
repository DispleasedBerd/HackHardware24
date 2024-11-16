import pygame
import sys

# Colors
TRACK_COLOR = (100, 100, 100)
HIT_ZONE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HackHardware24 - One Column")

#hit zone
hit_zone_y = SCREEN_HEIGHT - 100
hit_zone_height = 10

def create_track():
    screen.fill(BACKGROUND_COLOR)

    #track
    track_width = 100
    track_x = (SCREEN_WIDTH - track_width) // 2
    pygame.draw.rect(screen, TRACK_COLOR, (track_x, 0, track_width, SCREEN_HEIGHT))

    #hit zone
    pygame.draw.rect(screen, HIT_ZONE_COLOR, (track_x, hit_zone_y, track_width, hit_zone_height))