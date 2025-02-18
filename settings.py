import math

WIDTH = 1280
HEIGHT = 720
FPS = 60
MAX_RAY_DEPTH = 10
FOV = math.pi / 3
NUM_RAYS = WIDTH
DIST = NUM_RAYS / (2 * math.tan(FOV / 2))
PROJ_COEFF = DIST
SCALE = WIDTH / NUM_RAYS
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
PLAYER_ANGLE_SPEED = 1.5
PLAYER_SPEED = 3
MOUSE_SENSITIVITY = 0.002
PLAYER_RUNNING_SPEED = 5
MAX_HEALTH = 100