import pygame
import sys
import track

#score properties
score = 0
SCORE_COLOR = (255, 255, 0)

def update(points):
    global score
    score += points

def draw_score(screen):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(score_text,(20,20))

