import note, music, menu, track, score
import pygame
import sys

pygame.init()

#frame rate
clock = pygame.time.Clock()

def start_game():
    global note_y, score
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
                    if track.hit_zone_y - note.note_radius <= note_y <= track.hit_zone_y + track.hit_zone_height:
                        score = score + 1
                        note_y = -note.note_radius

        note_y = note_y + note.note_speed * dt

        if note_y > track.SCREEN_HEIGHT + note.note_radius:
            print("note missed, no score added.")
            note_y = -note.note_radius

        #print score onto screen
        score.update_score()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_game()