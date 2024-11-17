import note, menu, track, json, score
from score import Score
from note import Note, generate_notes_beatmap
from track import build_tracks, draw_tracks
import pygame
import sys
import leaderboard

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
        player_score.update_combo(screen)
        player_score.update_multiplier(screen)

        dt = clock.get_time() / 1000

        # Initialize a dictionary to track the pressed state of keys
        key_states = {track.input_key: False for track in tracks}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print(f"KEYDOWN: {pygame.key.name(event.key)}")
                for note in notes:
                    if event.key == tracks[0].input_key and note.track_index == tracks[0].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone():
                            print("Note hit in zone")
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                        else:
                            print("Note missed")
                            # player_score.reset_combo(screen)
                    elif event.key == tracks[1].input_key and note.track_index == tracks[1].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                        else:
                            print("Note missed")
                            # player_score.reset_combo(screen)
                    elif event.key == tracks[2].input_key and note.track_index == tracks[2].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                        else:
                            print("Note missed")
                            # player_score.reset_combo(screen)
                    elif event.key == tracks[3].input_key and note.track_index == tracks[3].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                        else:
                            print("Note missed")
                            # player_score.reset_combo(screen)
            if event.type == pygame.KEYUP:
                print(f"KEYUP: {pygame.key.name(event.key)}")
            
        
                        

        for note in notes:
            if note.active and current_time >= note.time:
                note.update_position(dt)
                note.draw(screen)

                if note.missed(SCREEN_HEIGHT):
                    note.active = False 
                    player_score.reset_combo(screen)

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
