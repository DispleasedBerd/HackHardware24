import pygame
import sys
import track

pygame.init()

class Score:
    def __init__(self):
        #score
        self.player_score = 0
        self.SCORE_COLOR = (255, 255, 0)
        self.font = pygame.font.SysFont(None,40)
        

    def update_score(self, screen):
        score_text = self.font.render(f"Score: {self.player_score}", True, self.SCORE_COLOR)
        screen.blit(score_text, (20,20))

    def add_score(self, points):
        self.player_score = self.player_score + points

