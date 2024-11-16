import pygame
import sys

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HackHardware24 - One Column")

# Colors
BACKGROUND_COLOR = (30, 30, 30)
NOTE_COLOR = (255, 255, 255)
TRACK_COLOR = (100, 100, 100)

#note properties
note_radius = 20
note_x = SCREEN_WIDTH // 2
note_y = 0  # Start at the top of the screen
note_speed = 200  # Pixels per second

#frame rate
clock = pygame.time.Clock()

#main loop
def main():
    global note_y
    running = True
    start_time = pygame.time.get_ticks()/1000

    while running:
        dt = clock.get_time() / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        note_y = note_y + note_speed * dt

        if note_y > SCREEN_HEIGHT + note_radius:
            note_y = -note_radius

        screen.fill(BACKGROUND_COLOR)

        #track
        track_width = 100
        track_x = (SCREEN_WIDTH - track_width) // 2
        pygame.draw.rect(screen, TRACK_COLOR, (track_x, 0, track_width, SCREEN_HEIGHT))

        pygame.draw.circle(screen, NOTE_COLOR, (note_x, int(note_y)), note_radius)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()