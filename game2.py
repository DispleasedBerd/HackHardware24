import note, music, menu, track, score
import pygame
import sys

pygame.init()
font = pygame.font.SysFont(None,40)
#frame rate
clock = pygame.time.Clock()

screen = track.create_track()

def start_game():
    menu.start_menu()
    global note_y, player_score
    player_score = 0
    running = True
    start_time = pygame.time.get_ticks()/1000

    while running:
        dt = clock.get_time() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #check if note in hit zone
                    if track.hit_zone_y - note.note_radius <= note.note_y <= track.hit_zone_y + track.hit_zone_height:
                        score.update(1)
                        note.reset_note()

        note.update_note_position(dt)

        if note.note_y > track.SCREEN_HEIGHT + note.note_radius:
            print("note missed, no score added.")
            note.reset_note()

        #update screen
        screen.fill(track.BACKGROUND_COLOR)
        track.draw_track()
        note.draw_note()
        score.draw_score(screen)

        pygame.display.flip()
        clock.tick(60)
  
    pygame.quit()
    sys.exit()  

if __name__ == "__main__":
    start_game()