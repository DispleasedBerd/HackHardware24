import pygame, track
import heapq as hq

# Constants
NOTE_COLOR = (255, 255, 255)
NOTE_RADIUS = 20
NOTE_SPEED = 200  # Pixels per second
TRACK_POSITIONS = ["LEFT", "DOWN", "UP", "RIGHT"]

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

class Note:

    def __init__(self, track, time, note_speed=NOTE_SPEED):
        """
        Initialize a Note object.
        :param track: Track object where the note belongs.
        :param time: Spawn time (in seconds) for the note.
        :param note_speed: Speed of the note falling.
        """
        self.x = track.x + track.width // 2  # Center of the track
        self.y = -50  # Start above the screen
        self.radius = NOTE_RADIUS
        self.speed = note_speed
        self.time = time  # Time when the note should appear
        self.active = True  # Whether the note is active
        self.color = NOTE_COLOR
        self.track_index = track.pos

    def update_position(self, dt):
        """Update the position of the note."""
        if self.active:
            self.y += self.speed * dt

    def draw(self, screen):
        """Draw the note on the screen."""
        if self.active:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def is_in_score_zone(self):
        #if track.HIT_ZONE_Y is None or track.HIT_ZONE_HEIGHT is None:
         #   print("Error: hit_zone_y or hit_zone_height not provided")
          #  return False
        return (
        track.HIT_ZONE_Y - self.radius - 10 <= self.y <= track.HIT_ZONE_Y + track.HIT_ZONE_HEIGHT + 10
        )

    def missed(self, screen_height):
        """Check if the note has moved off the screen."""
        if self.active and self.y > screen_height:
            self.active = False
            return True
        return False

    def calculate_score(self, hit_zone_y):
        """Calculate the score based on the distance from the hit zone."""
        max_score = 100
        distance = abs(self.y - hit_zone_y)
        return max_score * 2.7 ** (-distance)
    
def generate_notes_beatmap(beatmap_data, tracks):
    """
    Generate Note objects from the beatmap data.
    :param beatmap_data: List of dicts from the JSON beatmap.
    :param tracks: List of Track objects.
    :return: List of Note objects.
    """
    print(f"Generating notes with tracks: {tracks}")
    notes = []
    for entry in beatmap_data:
        track_idx = entry["track"]
        time = entry["time"]

        # Validate track index
        if track_idx < 0 or track_idx >= len(tracks):
            continue

        notes.append(Note(track=tracks[track_idx], time=time))
    return notes
