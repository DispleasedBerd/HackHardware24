import note, music, menu, track, score
import pygame
import sys

pygame.init()
font = pygame.font.SysFont(None,40)
#frame rate
clock = pygame.time.Clock()

def start_game():
    menu.start_menu()
    global note_y, player_score
    player_score = 0
    running = True
    start_time = pygame.time.get_ticks()/1000

    while running:
        dt = clock.get_time() / 1000

        track.create_track()
        note.create_note()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #check if note in hit zone
                    if track.hit_zone_y - note.note_radius <= note.note_y <= track.hit_zone_y + track.hit_zone_height:
                        player_score = player_score + 1
                        note.note_y = -note.note_radius

        note.note_y = note.note_y + note.note_speed * dt

        if note.note_y > track.SCREEN_HEIGHT + note.note_radius:
            print("note missed, no score added.")
            note_y = -note.note_radius

        #print score onto screen
        score.update_score(player_score)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_game()