import pygame

# Screen properties
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

# Track properties
CENTER = SCREEN_WIDTH / 2
TRACK_COLOR = (100, 100, 100)
TRACK_WIDTH = 100
TRACK_HEIGHT = SCREEN_HEIGHT
HIT_ZONE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)
TRACK_POSITIONS = ["LEFT", "DOWN", "UP", "RIGHT"]
TRACK_X = {"LEFT": CENTER - 215, "DOWN": CENTER - 105, "UP": CENTER + 5, "RIGHT": CENTER + 115}
INPUT = {
    "LEFT": pygame.K_LEFT,
    "DOWN": pygame.K_DOWN,
    "UP": pygame.K_UP,
    "RIGHT": pygame.K_RIGHT,
}

# Hit zone properties
HIT_ZONE_Y = SCREEN_HEIGHT - 100
HIT_ZONE_HEIGHT = 25


class Track:
    def __init__(self, pos, input_key):
        """
        Initialize a Track object.
        :param pos: The position of the track (e.g., "LEFT").
        :param input_key: The key associated with this track.
        """
        self.width = TRACK_WIDTH
        self.height = TRACK_HEIGHT
        self.color = TRACK_COLOR
        self.pos = pos
        self.x = TRACK_X[self.pos]
        self.input_key = input_key

    def draw(self, screen):
        """Draw the track and its hit zone."""
        # Draw the track
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.height))
        # Draw the hit zone
        pygame.draw.rect(
            screen,
            HIT_ZONE_COLOR,
            (self.x, HIT_ZONE_Y, self.width, HIT_ZONE_HEIGHT),
        )


def build_tracks():
    """
    Build and return a list of Track objects.
    """
    tracks = []
    for pos in TRACK_POSITIONS:
        input_key = INPUT[pos]
        tracks.append(Track(pos=pos, input_key=input_key))
    return tracks


def draw_tracks(screen, tracks):
    """Draw all tracks on the screen."""
    for track in tracks:
        track.draw(screen)