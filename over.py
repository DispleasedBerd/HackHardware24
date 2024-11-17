import pygame
import note

def isGameOver(notes):
    return all(note.is_processed(i) for i in range(note.num_notes))

def displayGameOver(screen):
    pygame.init()
    gameOverRect = pygame.Surface((480,620),pygame.SRCALPHA)
    gameOverRect.set_alpha(128)
    pygame.draw.rect(gameOverRect,(100,100,100),pygame.rect(0,0,480,620),border_radius=10)
    fontScore = pygame.font.Font(None,60)
    score = 100
    scoreText = fontScore.render(f'SCORE: {score}',True,(0,0,0))
    screen.blit(gameOverRect,(400,50)) 
    screen.blit(scoreText, (screen.get_width() // 2 - scoreText.get_width() // 2,
                    screen.get_height() // 6 - scoreText.get_height() // 2))
    pygame.display.update()