import note, menu, track, json
from score import Score
from note import Note, generate_notes_beatmap
from track import build_tracks, draw_tracks
import pygame
import sys

pygame.init()
font = pygame.font.SysFont(None, 40)

# Frame rate
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


def create_game():
    """Create and return the game window."""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HackHardware24 - Rhythm Game")
    return screen


def start_game(beatmap_path):
    """Main game loop."""
    global screen
    screen = create_game()

    if beatmap_path is None:
        print("No beatmap selected. Exiting...")
        pygame.quit()
        sys.exit()

    # Load the beatmap
    with open(beatmap_path, 'r') as f:
        beatmap_data = json.load(f)
    print(f"Loaded beatmap: {beatmap_path}")

    # Build tracks and generate notes
    tracks = build_tracks()
    notes = generate_notes_beatmap(beatmap_data, tracks)

    global player_score
    player_score = Score()

    running = True
    start_time = pygame.time.get_ticks() / 1000

    while running:
        current_time = pygame.time.get_ticks() / 1000 - start_time
        screen.fill(track.BACKGROUND_COLOR)

        # Draw tracks
        draw_tracks(screen, tracks)

        player_score.update_score(screen)

        dt = clock.get_time() / 1000

        for note in notes:
            if note.active and current_time >= note.time:
                note.update_position(dt)
                note.draw(screen)

                if note.missed(SCREEN_HEIGHT):
                    note.active = False 

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    selected_beatmap = menu.start_menu()
    if selected_beatmap:
        start_game(selected_beatmap)
    else:
        print("No beatmap selected.")
        pygame.quit()
        sys.exit()
