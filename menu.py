import pygame,sys
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
font = pygame.font.SysFont(None,100)

 
running = True
while running:
    mousePos = pygame.mouse.get_pos()
    menuText = font.render("Play", True, (255,255,255))
    screen.blit(menuText, (screen.get_width() // 2 - menuText.get_width() // 2,
                           screen.get_height() // 2 - menuText.get_height() // 2))

    click = False

    playButton = pygame.Rect(50,100,200,50)
    leaderButton = pygame.Rect(50,200,200,50)
    quitButton = pygame.Rect(50,300,200,50)

    pygame.draw.rect(screen, (0, 0, 0), playButton)
    pygame.draw.rect(screen, (0, 0, 0), leaderButton)
    pygame.draw.rect(screen, (0,0,0), quitButton)
    

    playText = font.render("Play", True, (255, 255, 255))
    leaderText = font.render("Leaderboard", True, (255, 255, 255))
    quitText = font.render("Quit", True, (255, 255, 255))

    if playButton.collidepoint(mousePos):
        pygame.draw.rect(screen, (100, 100, 100), playButton, 3)  # Highlight Play Button
    if leaderButton.collidepoint(mousePos):
        pygame.draw.rect(screen, (100, 100, 100), leaderButton, 3)  # Highlight Leaderboard Button
    if quitButton.collidepoint(mousePos):
        pygame.draw.rect(screen, (100, 100, 100), quitButton, 3)  # Highlight Quit Button


    if playButton.collidepoint(mousePos):
        if click:
            #game()
            print('Play')
    
    if leaderButton.collidepoint(mousePos):
        if click:
            #leaderboard()
            print('Leaderboard')

    if quitButton.collidepoint(mousePos):
        if click:
            running=False

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

pygame.display.quit()
pygame.quit()
sys.exit()
