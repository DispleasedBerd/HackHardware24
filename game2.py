import menu, track, json, score, gameOver, beatmap
import note as nt
import heapq as hq
from score import Score
from note import generate_notes_beatmap
from track import build_tracks, draw_tracks, HIT_ZONE_HEIGHT, HIT_ZONE_Y, BACKGROUND_COLOR
import pygame
import sys
import leaderboard
import pygame.mixer

pygame.init()
font = pygame.font.SysFont(None, 40)
muted = False

# Frame rate
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

def create_game():
    """Create and return the game window."""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HackHardware24 - Rhythm Game")
    return screen

def start_game(beatmap_path):
    """Main game loop with music."""
    global screen
    screen = create_game()

    if beatmap_path is None:
        print("No beatmap selected. Exiting...")
        pygame.quit()
        sys.exit()

    # Load the beatmap
    with open(beatmap_path, 'r') as f:
        beatmap_data = json.load(f)

    # Debugging output
    print("Beatmap Data:", beatmap_data)

    # Check for valid structure
    if not isinstance(beatmap_data, dict) or "audio" not in beatmap_data or "notes" not in beatmap_data:
        print("Invalid beatmap format. Expected keys: 'audio', 'notes'. Exiting...")
        pygame.quit()
        sys.exit()

    # Extract audio file name and notes
    audio_file = beatmap_data["audio"]
    notes_data = beatmap_data["notes"]

    print("Beatmap Notes Data:", notes_data)

    # Initialize music
    audio_path = f"./assets/audio/{audio_file}"
    pygame.mixer.init()
    try:
        if not muted:
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error loading audio file: {e}")
        pygame.quit()
        sys.exit()

    # Generate notes from beatmap
    tracks = build_tracks()
    notes = generate_notes_beatmap(notes_data, tracks)  # Ensure notes_data is a list of dictionaries

    global player_score
    player_score = Score()

    running = True
    start_time = pygame.time.get_ticks() / 1000

    while running:
        current_time = pygame.time.get_ticks() / 1000 - start_time
        dt = clock.tick(60) / 1000  # Limit frame rate to 60 FPS

        # Clear screen with background color
        screen.fill(track.BACKGROUND_COLOR)

        # Draw tracks
        draw_tracks(screen, tracks)

        # Update and display the score
        player_score.update_score(screen)
        player_score.update_combo(screen)
        player_score.update_multiplier(screen)
        player_score.update_lives(screen)
        # closest = nt.find_closest(notes)

        dt = clock.get_time() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                key_matched = False

                for note in notes:
                    if event.key == tracks[0].input_key and note.track_index == tracks[0].pos:
                        key_matched = True
                        print("1")
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                            break
                    elif event.key == tracks[1].input_key and note.track_index == tracks[1].pos:
                        print("2")
                        key_matched = True
                            #check if note in hit zone
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                            break
                    elif event.key == tracks[2].input_key and note.track_index == tracks[2].pos:
                        #check if note in hit zone
                        print("3")
                        key_matched=True
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)
                            break
                    elif event.key == tracks[3].input_key and note.track_index == tracks[3].pos:
                        #check if note in hit zone
                        print("4")
                        key_matched=True
                        if note.is_in_score_zone():
                            player_score.add_score(player_score.calculate_score(note), note, screen)
                            player_score.add_combo(screen)  
                            break      

                # if not key_matched:
                #     print(f"Note missed at y={note.y}")
                #     player_score.lives -= 1
                #     player_score.reset_combo(screen)
                #     if player_score.lives <= 0:
                #         gameOver.displayGameOver(screen,player_score)

        for note in notes:
            if note.active and current_time >= note.time:
                note.update_position(dt)
                note.draw(screen)

                if note.missed(SCREEN_HEIGHT):
                    note.active = False 
                    player_score.reset_combo(screen)
                    # player_score.lives -= 1  # Deduct a life
                    if player_score.lives <= 0:
                        gameOver.displayGameOver(screen, player_score)
                        # pygame.time.delay(60000
                        
        # Refresh the display
        pygame.display.flip()

    # Stop music when the game exits
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    #selected_beatmap = menu.start_menu()
    menu.start_menu()
    