import pygame,sys, game2
import leaderboard, game2

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
font = pygame.font.SysFont(None,40)
clock = pygame.time.Clock()
skibidi = pygame.image.load("Assets/Skibidi.png")
skibidi = pygame.transform.scale(skibidi,(1280,720))

def start_menu():
    running = True
    while running:
        mousePos = pygame.mouse.get_pos()
        menuText = font.render("Play", True, (255,255,255))
        screen.blit(menuText, (screen.get_width() // 2 - menuText.get_width() // 2,
                            screen.get_height() // 2 - menuText.get_height() // 2))

        screen.blit(skibidi,(0,0))

        click = False

        playButton = pygame.Rect(50,150,200,50)
        leaderButton = pygame.Rect(50,300,200,50)
        quitButton = pygame.Rect(50,450,200,50)
        settingsButton = pygame.Rect(50,600,200,50)

        pygame.draw.rect(screen, (255, 0, 0), playButton)
        pygame.draw.rect(screen, (255, 0, 0), leaderButton)
        pygame.draw.rect(screen, (255,0,0), quitButton)
        pygame.draw.rect(screen, (255,0,0), settingsButton)

        

        playText = font.render("Play", True, (255, 255, 255))
        leaderText = font.render("Leaderboard", True, (255, 255, 255))
        quitText = font.render("Quit", True, (255, 255, 255))
        settingsText = font.render("Settings", True, (255, 255, 255))

        if playButton.collidepoint(mousePos):
            pygame.draw.rect(screen, (100, 100, 100), playButton, 3)  # Highlight Play Button
        if leaderButton.collidepoint(mousePos):
            pygame.draw.rect(screen, (100, 100, 100), leaderButton, 3)  # Highlight Leaderboard Button
        if quitButton.collidepoint(mousePos):
            pygame.draw.rect(screen, (100, 100, 100), quitButton, 3)  # Highlight Quit Button
        if settingsButton.collidepoint(mousePos):
            pygame.draw.rect(screen, (100, 100, 100), settingsButton, 3)  # Highlight Settings Button
        

        screen.blit(playText, (playButton.x + (playButton.width - playText.get_width()) // 2,
                            playButton.y + (playButton.height - playText.get_height()) // 2))
        screen.blit(leaderText, (leaderButton.x + (leaderButton.width - leaderText.get_width()) // 2,
                                leaderButton.y + (leaderButton.height - leaderText.get_height()) // 2))
        screen.blit(quitText, (quitButton.x + (quitButton.width - quitText.get_width()) // 2,
                            quitButton.y + (quitButton.height - quitText.get_height()) // 2))
        screen.blit(settingsText, (settingsButton.x + (settingsButton.width - settingsText.get_width()) // 2,
                            settingsButton.y + (settingsButton.height - settingsText.get_height()) // 2))

        pygame.display.update()
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if playButton.collidepoint(mousePos):
            if click:
                #g start game
                return
        
        if leaderButton.collidepoint(mousePos):
            if click:
                leaderboard()

        if quitButton.collidepoint(mousePos):
            if click:
                running=False

        if settingsButton.collidepoint(mousePos):
            if click:
                print("settings")

    pygame.display.quit()
    pygame.quit()
    sys.exit()
