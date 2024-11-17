import note, menu, track, json, score
from score import Score
from note import generate_notes_beatmap
from track import build_tracks, draw_tracks, HIT_ZONE_HEIGHT, HIT_ZONE_Y, BACKGROUND_COLOR
import pygame
import sys
import leaderboard
import pygame.mixer

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

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Check if the pressed key matches a track's input key
                for track_obj in tracks:
                    if event.key == track_obj.input_key:
                        # Check for active notes in the hit zone for this track
                        for note in notes:
                            if (
                                note.active
                                and note.track_index == track_obj.pos
                                and note.is_in_score_zone(track.HIT_ZONE_Y, track.HIT_ZONE_HEIGHT)
                            ):
                                print("Note hit!")
                                player_score.add_score(1, screen)
                                note.active = False  # Deactivate the note
                                break

        # Draw tracks
        draw_tracks(screen, tracks)

        # Update and display the score
        player_score.update_score(screen)

        # Update and draw notes
        for note in notes:
            if note.active and current_time >= note.time:
                note.update_position(dt)
                note.draw(screen)

                if note.missed(track.SCREEN_HEIGHT):
                    print("Note missed!")
                    note.active = False

        # Refresh the display
        pygame.display.flip()

    # Stop music when the game exits
    pygame.mixer.music.stop()
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
