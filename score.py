import pygame
import sys
import track


#score
score = 0
SCORE_COLOR = (255, 255, 0)
font = pygame.font.Font(None, 36)

def update_score():
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    track.screen.blit(score_text, (20,20))


def is_in_score_zone(note):
    if track.hit_zone_y - note.note_radius <= note.note_y <= track.hit_zone_y + track.hit_zone_height:
        return True
    else:
        return False
    
def calculate_score(note):
    max_score = 100
    distance = abs(note.note_y-track.hit_zone_y)
    score = max_score*2.7**(-distance)
    