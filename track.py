import pygame
import sys

#track properties
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 750
TRACK_COLOR = (100, 100, 100)
TRACK_WIDTH = SCREEN_WIDTH // 4
TRACK_HEIGHT = SCREEN_HEIGHT
HIT_ZONE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)
TRACK_WIDTH = 100
TRACK_NUM = 4
track_x = {"LEFT":185,"DOWN":295,"UP":405,"RIGHT":515}
INPUT = {"LEFT": pygame.K_LEFT,"DOWN": pygame.K_DOWN,"UP":pygame.K_UP,"RIGHT":pygame.K_RIGHT}


#hit zone
hit_zone_y = SCREEN_HEIGHT - 100
hit_zone_height = 25

def build_tracks():
    left = Track("LEFT")
    down = Track("DOWN")
    up = Track("UP")
    right = Track("RIGHT")
    tracks = [left,down, up, right]
    return tracks

def draw_track(screen, tracks):
        for t in tracks:
            pygame.draw.rect(screen, t.TRACK_COLOR, (t.x, 0, t.TRACK_WIDTH, SCREEN_HEIGHT))

            #hit zone
            pygame.draw.rect(screen, HIT_ZONE_COLOR, (t.x, hit_zone_y, t.TRACK_WIDTH, hit_zone_height))

        return tracks
class Track:
    def __init__(self, pos):
        self.TRACK_WIDTH = 100 # SCREEN_WIDTH // 4
        self.TRACK_HEIGHT = SCREEN_HEIGHT # maybe change?
        self.TRACK_COLOR = TRACK_COLOR
        self.pos = pos # left, right, up, down
        self.x = track_x[self.pos]
        self.INPUT = INPUT[self.pos]

    
    