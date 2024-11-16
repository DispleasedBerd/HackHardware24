import note, music, menu, track 
from score import Score
from note import Note
from track import Track
import numpy as np
import pygame
import sys

pygame.init()
font = pygame.font.SysFont(None,40)
#frame rate
clock = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 750


def create_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HackHardware24 - One Column")
    return screen

def start_game():
    global screen
    screen = create_game()
    menu.start_menu()
    
    tracks = track.draw_track(screen, track.build_tracks())
    global note1
    note1 = Note(tracks[0])
    note2 = Note(tracks[1])
    global player_score
    player_score = Score()
    running = True
    start_time = pygame.time.get_ticks()/1000

    while running:
        player_score.update_score(screen)
        dt = clock.get_time() / 1000
        # if clock.get_time() % 250 == 0:
            
        #     print('second')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == tracks[0].INPUT:
                    #check if note in hit zone
                    if track.hit_zone_y - note.note_radius <= note1.note_y <= track.hit_zone_y + track.hit_zone_height:
                        player_score.update_score(screen)
                        player_score.add_score(1)
                        note1.reset_note()
                if event.key == tracks[1].INPUT:
                    #check if note in hit zone
                    if track.hit_zone_y - note.note_radius <= note2.note_y <= track.hit_zone_y + track.hit_zone_height:
                        player_score.update_score(screen)
                        player_score.add_score(1)
                        note2.reset_note()

        note1.update_note_position(dt)
        note2.update_note_position(dt)

        if note1.note_y > track.SCREEN_HEIGHT + note1.note_radius:
            print("note missed, no score added.")
            note1.reset_note()
        if note2.note_y > track.SCREEN_HEIGHT + note2.note_radius:
            print("note missed, no score added.")
            note2.reset_note()

        #update screen
        screen.fill(track.BACKGROUND_COLOR)
        track.draw_track(screen)
        note1.draw_note(screen)
        note2.draw_note(screen)
        # player_score.draw_score(screen)

        pygame.display.flip()
        clock.tick(60)
  
    pygame.quit()
    sys.exit()  

if __name__ == "__main__":
    start_game()