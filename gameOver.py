import pygame, menu, leaderboard
import note

fontSmall = pygame.font.Font(None,40)
fontGlow = pygame.font.Font(None,45)

def isGameOver(notes):
    return all(note.is_processed(i) for i in range(note.num_notes))

def displayGameOver(screen, player_score):
    pygame.init()
    leaderboard.leaderboard.players = leaderboard.leaderboard.players + 1
    leaderboard.leaderboard.add_score(f"Player {leaderboard.leaderboard.players}", player_score.player_score)

    click = False
    running = True
    while running:
        mousePos = pygame.mouse.get_pos()

        gameOverRect = pygame.Surface((480,620),pygame.SRCALPHA)
        gameOverRect.set_alpha(256)
        pygame.draw.rect(gameOverRect, (200,200,200), pygame.Rect(0,0,480,620), border_radius=10)
        fontScore = pygame.font.Font(None, 60)
        scoreText = fontScore.render(f'SCORE: {player_score.player_score}', True,(0,0,0))
        screen.blit(gameOverRect, (400,50))
        screen.blit(scoreText, (screen.get_width() // 2 - scoreText.get_width() // 2,
                                screen.get_height() // 6 - scoreText.get_height() // 2))
        
        for rank in range(1,6):
            rankText = fontSmall.render(f'{rank}. ',True,(0,0,0))
            screen.blit(rankText,(480, 100+100*rank))
            # rankGlow = fontGlow.render(f'{rank}. ',True,(255,255,255))
            # screen.blit(rankGlow,(480, 100+50*rank))


        for rank,entry in enumerate(leaderboard.leaderboard.leaderboard,start=1):
            name = entry['name']
            score = entry['score']
            nameText = fontSmall.render(f'{name}',True,(0,0,0))
            scoreText = fontSmall.render(f'{score}',True,(0,0,0))
            screen.blit(nameText, (screen.get_width() // 2 - nameText.get_width() // 2 - 80, 100+100*rank))
            screen.blit(scoreText,(screen.get_width() // 2 - scoreText.get_width() // 2 + 120, 100+100*rank))

            # nameGlow = fontGlow.render(f'{name}',True,(255,255,255))
            # scoreGlow = fontGlow.render(f'{score}',True,(255,255,255))
            # screen.blit(nameGlow, (screen.get_width() // 2 - nameText.get_width() // 2 - 80, 100+50*rank))
            # screen.blit(scoreGlow,(screen.get_width() // 2 - scoreText.get_width() // 2 + 120, 100+50*rank))


            color=(255,255,255)
            pygame.draw.rect(screen,color,pygame.Rect(400,50,480,620),2,3)
        
        backButton = pygame.Rect((50,600,200,50))
        pygame.draw.rect(screen, (255,255,255), backButton,2,3)
        backText = fontSmall.render("back", True, (255, 255, 255))
        if backButton.collidepoint(mousePos):
            pygame.draw.rect(screen, (100, 100, 100), backButton, 2,3)  # Highlight Quit Button
            backText = fontSmall.render("back", True, (100, 100, 100))

        screen.blit(backText, (backButton.x + (backButton.width - backText.get_width()) // 2,
                            backButton.y + (backButton.height - backText.get_height()) // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        if backButton.collidepoint(mousePos):
            if click:
                menu.start_menu()
                click = False
        
        pygame.display.update()