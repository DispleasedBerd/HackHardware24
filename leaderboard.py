# Leaderboard implementation allowing one player to occupy multiple spots
import pygame,sys,menu



def displayLeaderboard(leaderboard):

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Leaderboard")
    font = pygame.font.SysFont(None,80)
    clock = pygame.time.Clock()
    gradient = pygame.image.load("Assets/gradient.jpg")
    gradient = pygame.transform.scale(gradient,(1280,720))

    running = True
    while running:
        mousePos = pygame.mouse.get_pos()

        screen.blit(gradient,(0,0))
        menuText = font.render("HIGH SCORES", True, (255,255,255))

        click = False

        # LeaderRect = pygame.Rect(screen.get_width()//2 - menuText.get_width() //2 ,screen.get_height()//6 - menuText.get_height() // 2, menuText.get_width(),menuText.get_height())

        #pygame.draw.rect(screen, (255, 0, 0), LeaderRect)

        screen.blit(menuText, (screen.get_width() // 2 - menuText.get_width() // 2,
                            screen.get_height() // 6 - menuText.get_height() // 2))
        

        fontSmall = pygame.font.Font(None,40)
        fontGlow = pygame.font.Font(None,45)
        for rank,entry  in enumerate(leaderboard.leaderboard,start=1):
            name = entry['name']
            score = entry['score']
            nameText = fontSmall.render(f'{name}',True,(0,0,0))
            scoreText = fontSmall.render(f'{score}',True,(0,0,0))
            # rankText = fontSmall.render(f'{rank}. ',True,(0,0,0))
            # screen.blit(nameText, (screen.get_width() // 2 - nameText.get_width() // 2 - 80, 100+100*rank))
            # screen.blit(scoreText,(screen.get_width() // 2 - scoreText.get_width() // 2 + 120, 100+100*rank))
            # screen.blit(rankText,(480, 100+100*rank))

            nameGlow = fontGlow.render(f'{name}',True,(255,255,255))
            scoreGlow = fontGlow.render(f'{score}',True,(255,255,255))
            rankGlow = fontGlow.render(f'{rank}. ',True,(255,255,255))
            screen.blit(nameGlow, (screen.get_width() // 2 - nameText.get_width() // 2 - 80, 100+100*rank))
            screen.blit(scoreGlow,(screen.get_width() // 2 - scoreText.get_width() // 2 + 120, 100+100*rank))
            screen.blit(rankGlow,(480, 100+100*rank))


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




        pygame.display.update()
        clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        
        if backButton.collidepoint(mousePos):
            if click:
                menu.start_menu()
    
    pygame.display.quit()
    pygame.quit()
    sys.exit()


class Leaderboard:

    def __init__(self):
        self.leaderboard = []  # List to store player-score pairs
        self.players = 0

    def add_score(self, name, score):
        # Add a new entry for the player's score
        self.leaderboard.append({"name": name, "score": score})
        # leaderboard.add_score("Player 1", 0)
        # leaderboard.add_score("Player 2", 0)
        # leaderboard.add_score("Player 3", 0)  # Alice can occupy multiple spots
        # leaderboard.add_score("Player 4", 0)
        # leaderboard.add_score("Allan", 0)
        # leaderboard.add_score("Player 6", 0)  # Adding more entries will keep only top 5
        # leaderboard.add_score("Player 7", 0)

        # Sort the leaderboard by score in descending order and keep only top 5 entries
        self.leaderboard = sorted(self.leaderboard, key=lambda entry: entry["score"], reverse=True)[:5]

    def display(self):
        print("Leaderboard (Top 5 Scores):")
        for rank, entry in enumerate(self.leaderboard, start=1):
            print(f"{rank}. {entry['name']}: {entry['score']}")

# Usage
# leaderboard = Leaderboard()
# leaderboard.add_score("Player 1", 0)
# leaderboard.add_score("Player 2", 0)
# leaderboard.add_score("Player 3", 0)  # Alice can occupy multiple spots
# leaderboard.add_score("Player 4", 0)
# leaderboard.add_score("Allan", 0)
# leaderboard.add_score("Player 6", 0)  # Adding more entries will keep only top 5
# leaderboard.add_score("Player 7", 0)


leaderboard = Leaderboard()











