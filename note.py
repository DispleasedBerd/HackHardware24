import pygame, track
import heapq as hq

# Constants
NOTE_COLOR = (255, 255, 255)
NOTE_RADIUS = 20
NOTE_SPEED = 200  # Pixels per second
TRACK_POSITIONS = ["LEFT", "DOWN", "UP", "RIGHT"]

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720

def find_closest(notes):
    heap1 = []
    heap2 = []
    heap3 = []
    heap4 = []
    closest = {TRACK_POSITIONS[0]: heap1,
                TRACK_POSITIONS[1]: heap2,
                TRACK_POSITIONS[2]: heap3,
                TRACK_POSITIONS[3]: heap4
                }
    for note in notes:
        height = SCREEN_HEIGHT-note.y
        if note.track_index == TRACK_POSITIONS[0]:
            hq.heappush(closest[TRACK_POSITIONS[0]], height)
        elif note.track_index == TRACK_POSITIONS[1]:
            hq.heappush(closest[TRACK_POSITIONS[1]], height)
        elif note.track_index == TRACK_POSITIONS[2]:
            hq.heappush(closest[TRACK_POSITIONS[2]], height)
        elif note.track_index == TRACK_POSITIONS[3]:
            hq.heappush(closest[TRACK_POSITIONS[3]], height)
        
    return closest

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

    def is_in_score_zone(self, hit_zone_y=None, hit_zone_height=None):
        if hit_zone_y is None or hit_zone_height is None:
            print("Error: hit_zone_y or hit_zone_height not provided")
            return False
        return (
        hit_zone_y - self.radius - 10 <= self.y <= hit_zone_y + hit_zone_height + 10
        )

    def missed(self, screen_height):
        """Check if the note has moved off the screen."""
        return self.y > screen_height

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
