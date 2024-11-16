import pygame
import sys
import track

pygame.init()

#score
score = 0
SCORE_COLOR = (255, 255, 0)
font = pygame.font.SysFont(None,40)

def update_score(player_score):
    score_text = font.render(f"Score: {player_score}", True, SCORE_COLOR)
    track.screen.blit(score_text, (20,20))

