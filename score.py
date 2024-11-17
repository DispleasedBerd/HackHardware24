import pygame
import sys
import track, note

pygame.init()

class Score:
    def __init__(self):
        #score
        self.combo = 0
        self.multiplier = 1
        self.player_score = 0
        self.SCORE_COLOR = (255, 255, 0)
        self.font = pygame.font.SysFont(None,40)
        
    def calculate_score(self, i):    
        center = track.hit_zone_y+track.hit_zone_height/2
        max_score = 100
        distance = abs(note.note_y[i]-center)
        score = self.multiplier*((track.hit_zone_height/2) // (distance+1) + 1)
        return score

    def update_score(self, screen):
        score_text = self.font.render(f"Score: {self.player_score}", True, self.SCORE_COLOR)
        screen.blit(score_text, (20,20))

    def add_score(self, points, screen):
        self.player_score = self.player_score + points
        self.update_score(screen)

    def update_combo(self, screen):
        combo_text = self.font.render(f"Combo: {self.combo}", True, self.SCORE_COLOR)
        screen.blit(combo_text, (20,50))

    def update_multiplier(self, screen):
        multiplier_text = self.font.render(f"Multiplier: x{self.multiplier}", True, self.SCORE_COLOR)
        screen.blit(multiplier_text, (20,80))
    

    def add_combo(self, screen):
        self.combo = self.combo + 1
        if self.combo % 5 == 0 and self.multiplier < 4:
            self.multiplier = self.multiplier + 0.25
            self.update_multiplier(screen)
        self.update_combo(screen)
            
    
    def reset_combo(self, screen):
        self.combo = 0
        self.multiplier = 1
        self.update_combo(screen)


