import pygame,sys, game2, leaderboard, os

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
font = pygame.font.SysFont(None,40)
clock = pygame.time.Clock()
skibidi = pygame.image.load("Assets/Skibidi.png")
skibidi = pygame.transform.scale(skibidi,(1280,720))

def get_beatmap_files(beatmap_folder):
    return [file for file in os.listdir(beatmap_folder) if file.endswith('_beatmap.json')]

def song_selection_menu(beatmap_folder):
    beatmaps = get_beatmap_files(beatmap_folder)

    if not beatmaps:
        print("No beatmaps found!")
        return None

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(skibidi, (0, 0))

        mouse_pos = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        buttons = []

        for idx, beatmap in enumerate(beatmaps):
            song_name = os.path.splitext(beatmap.replace("_beatmap", ""))[0]
            song_text = font.render(f"{idx + 1}. {song_name}", True, (255, 255, 255))
            text_rect = song_text.get_rect(center=(screen.get_width() // 2, 200 + idx * 50))
            screen.blit(song_text, text_rect)
            buttons.append((text_rect, beatmap))

        for rect, beatmap in buttons:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)  # Highlight button
                if click:
                    return os.path.join(beatmap_folder, beatmap)  # Return selected beatmap

        pygame.display.update()
        clock.tick(60)


def start_menu():
    running = True
    while running:
        screen.blit(skibidi, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # Define buttons
        play_button = pygame.Rect(50, 150, 200, 50)
        leader_button = pygame.Rect(50, 300, 200, 50)
        settings_button = pygame.Rect(50, 450, 200, 50)
        quit_button = pygame.Rect(50, 600, 200, 50)

        for button in [play_button, leader_button, settings_button, quit_button]:
            shadow = button.copy()
            shadow.x += 1
            shadow.y += 1
            pygame.draw.rect(screen, (50,50,50), shadow, border_radius = 20)
            pygame.draw.rect(screen, (250,0,0), button, border_radius = 20)

        if play_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (255,50,50), play_button, border_radius = 20)

        # Draw buttons
        #pygame.draw.rect(screen, (255, 0, 0), play_button)
        #pygame.draw.rect(screen, (255, 0, 0), leader_button)
        #pygame.draw.rect(screen, (255, 0, 0), settings_button)
        #pygame.draw.rect(screen, (255, 0, 0), quit_button)

        text_data = [
            ("Play", play_button),
            ("Leaderboard", leader_button),
            ("Settings", settings_button),
            ("Quit", quit_button),
        ]
        for text, button in text_data:
            shadow_text = font.render(text, True, (50, 50, 50))  # Shadow color
            main_text = font.render(text, True, (255, 255, 255))  # Main text color

            shadow_x = button.x + (button.width - shadow_text.get_width()) // 2 + 2  # Slight offset for shadow
            shadow_y = button.y + (button.height - shadow_text.get_height()) // 2 + 2

            main_x = button.x + (button.width - main_text.get_width()) // 2
            main_y = button.y + (button.height - main_text.get_height()) // 2

            screen.blit(shadow_text, (shadow_x, shadow_y))
            screen.blit(main_text, (main_x, main_y))
        """
        # Render text
        play_text = font.render("Play", True, (255, 255, 255))
        leader_text = font.render("Leaderboard", True, (255, 255, 255))
        settings_text = font.render("Settings", True, (255, 255, 255))
        quit_text = font.render("Quit", True, (255, 255, 255))
        
        screen.blit(play_text, (play_button.x + (play_button.width - play_text.get_width()) // 2,
                                play_button.y + (play_button.height - play_text.get_height()) // 2))
        screen.blit(leader_text, (leader_button.x + (leader_button.width - leader_text.get_width()) // 2,
                                  leader_button.y + (leader_button.height - leader_text.get_height()) // 2))
        screen.blit(settings_text, (settings_button.x + (settings_button.width - settings_text.get_width()) // 2,
                                    settings_button.y + (settings_button.height - settings_text.get_height()) // 2))
        screen.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2,
                                quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
        """
        #game title
        title_font = pygame.font.SysFont(None, 80)
        title_text = title_font.render("BeatMaxx", True, (255,255,255))
        title_x = screen.get_width() - title_text.get_width() - 50
        title_y = (screen.get_height() // 2) - (title_text.get_height() // 2)
        screen.blit(title_text,(title_x, title_y))

        pygame.display.update()
        clock.tick(60)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        # Handle button clicks
        if play_button.collidepoint(mouse_pos) and click:
            beatmap_folder = "./assets/beatmaps"
            selected_beatmap = song_selection_menu(beatmap_folder)
            game2.start_game(selected_beatmap)

        if leader_button.collidepoint(mouse_pos) and click:
            leaderboard.displayLeaderboard(leaderboard.leaderboard)

        if settings_button.collidepoint(mouse_pos) and click:
            print("Settings")

        if quit_button.collidepoint(mouse_pos) and click:
            game2.quit = True
            pygame.quit()
            sys.exit()

