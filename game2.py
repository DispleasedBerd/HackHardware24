import note, music, menu, track, json
from score import Score
from note import Note
from track import Track
import numpy as np
import pygame
import sys
import leaderboard

pygame.init()
font = pygame.font.SysFont(None,40)
#frame rate
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720


def create_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HackHardware24 - One Column")
    return screen

def start_game(beatmap_path):
    global screen
    screen = create_game()

    if beatmap_path is None:
        print("no beatmap selected. exiting")
        pygame.quit()
        sys.exit()

    with open(beatmap_path, 'r') as f:
        beatmap_data = json.load(f)
    print(f"Loaded beatmap: {beatmap_path}")

    tracks = track.draw_track(screen, track.build_tracks())
    note.build_notes(tracks)

    global player_score
    player_score = Score()

    tracks = track.draw_track(screen, track.build_tracks())
    note.build_notes(tracks)

    running = True
    start_time = pygame.time.get_ticks()/1000

    while running:
        player_score.update_score(screen)
        dt = clock.get_time() / 1000
        # if clock.get_time() % 250 == 0:
            
        # print('second')
            # print(note.is_in_score_zone(i))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                for i in range(note.num_notes): # hard coded here
                    if event.key == tracks[0].INPUT and note.get_note_track(i) == tracks[0].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone(i):
                            player_score.update_score(screen)
                            player_score.add_score(note.calculate_score(i))
                            note.respawn_note(i)
                    if event.key == tracks[1].INPUT and note.get_note_track(i) == tracks[1].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone(i):
                            player_score.update_score(screen)
                            player_score.add_score(note.calculate_score(i))
                            note.respawn_note(i)
                    if event.key == tracks[2].INPUT and note.get_note_track(i) == tracks[2].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone(i):
                            player_score.update_score(screen)
                            player_score.add_score(note.calculate_score(i))
                            note.respawn_note(i)
                    if event.key == tracks[3].INPUT and note.get_note_track(i) == tracks[3].pos:
                        #check if note in hit zone
                        if note.is_in_score_zone(i):
                            player_score.update_score(screen)
                            player_score.add_score(note.calculate_score(i))
                            note.respawn_note(i)

        if player_score.score == 3:
            name = 'Allen'
            leaderboard.leaderboard.add_score(name,player_score.score)
            leaderboard.displayLeaderboard()
                    

        for i in range(note.num_notes):
            note.update_note_position(i, dt)

            if note.missed_note(i):
                print("note missed, no score added.")
                note.respawn_note(i)
                # note.reset_note(i)

            #update screen
            
            note.draw_note(i, screen)

            # player_score.draw_score(screen)

        pygame.display.update()

        screen.fill(track.BACKGROUND_COLOR)
        track.draw_track(screen, tracks)
        clock.tick(60)
  
    pygame.quit()
    sys.exit()  

if __name__ == "__main__":
    selected_beatmap = menu.start_menu()
    if selected_beatmap:
        start_game(selected_beatmap)
    else:
        print("no beatmap selected..")
        pygame.quit()
        sys.exit()