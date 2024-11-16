import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
font = pygame.font.SysFont(None,20)


while True:
    screen.fill("blue")
    mousePos = pygame.mouse.get_pos()
    menuText = font.render("SKibidi Rizz", True, (255,255,255))
    screen.blit(menuText, (screen.get_width() // 2 - menuText.get_width() // 2,
                           screen.get_height() // 2 - menuText.get_height() // 2))
    pygame.display.update()




pygame.quit()
