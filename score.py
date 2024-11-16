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

