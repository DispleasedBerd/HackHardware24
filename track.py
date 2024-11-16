import pygame
import sys

#track properties
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 750
TRACK_COLOR = (100, 100, 100)
HIT_ZONE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)
TRACK_WIDTH = 100
TRACK_NUM = 4

#hit zone
hit_zone_y = SCREEN_HEIGHT - 100
hit_zone_height = 10

def create_track():
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HackHardware24 - One Column")
    return screen

def draw_track():
    for i in range(TRACK_NUM):
        track_x = i*TRACK_WIDTH

        pygame.draw.rect(screen, TRACK_COLOR, (track_x, 0, TRACK_WIDTH, SCREEN_HEIGHT))

        #hit zone
        pygame.draw.rect(screen, HIT_ZONE_COLOR, (track_x, hit_zone_y, TRACK_WIDTH, hit_zone_height))