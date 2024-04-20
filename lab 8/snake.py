import random
import pygame
import sys

pygame.init()
pygame.font.init()

# Setting up the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 680
TILE_SIZE = 40
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 20))

# Configuring time and text display
game_clock = pygame.time.Clock()
game_font = pygame.font.SysFont(pygame.font.get_default_font(), 27)

# Defining alternative basic colors
COLOR_RED = (200, 0, 100)    # A deep pink rather than bright red
COLOR_BLACK = (50, 50, 50)   # A dark gray instead of pure black
COLOR_BLUE = (100, 100, 250) # A softer blue
COLOR_GREEN = (0, 200, 150)  # A turquoise shade
COLOR_WHITE = (230, 230, 250) # A light lavender (off-white)

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.segments = [Coordinate(SCREEN_WIDTH // TILE_SIZE // 2, SCREEN_HEIGHT // TILE_SIZE // 2)]

    def render(self):
        # Rendering the head
        pygame.draw.rect(
            DISPLAY,
            COLOR_RED,
            pygame.Rect(
                self.segments[0].x * TILE_SIZE,
                self.segments[0].y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )
        )

        # Rendering the body
        for segment in self.segments[1:]:
            pygame.draw.rect(
                DISPLAY,
                COLOR_BLUE,
                pygame.Rect(
                    segment.x * TILE_SIZE,
                    segment.y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE,
                )
            )

    def update_position(self, dx, dy):
        new_head = Coordinate(self.segments[0].x + dx, self.segments[0].y + dy)
        self.segments = [new_head] + self.segments[:-1]

        # Ending game if the snake bites itself
        if any(new_head.x == seg.x and new_head.y == seg.y for seg in self.segments[1:]):
            end_game()

        # Boundary collision check
        if not (0 <= new_head.x < SCREEN_WIDTH // TILE_SIZE) or not (0 <= new_head.y < SCREEN_HEIGHT // TILE_SIZE):
            end_game()

    def detect_food_collision(self, food):
        return self.segments[0].x == food.position.x and self.segments[0].y == food.position.y

class Food:
    def __init__(self):
        self.position = Coordinate(random.randint(0, SCREEN_WIDTH // TILE_SIZE - 1), random.randint(0, SCREEN_HEIGHT // TILE_SIZE - 1))

    def draw(self):
        pygame.draw.rect(
            DISPLAY,
            COLOR_GREEN,
            pygame.Rect(
                self.position.x * TILE_SIZE,
                self.position.y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE,
            )
        )

    def respawn(self, snake_segments):
        while True:
            self.position = Coordinate(random.randint(0, SCREEN_WIDTH // TILE_SIZE - 1), random.randint(0, SCREEN_HEIGHT // TILE_SIZE - 1))
            if all(self.position.x != seg.x or self.position.y != seg.y for seg in snake_segments):
                break

def draw_playing_area():
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(DISPLAY, COLOR_WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(DISPLAY, COLOR_WHITE, (0, y), (SCREEN_WIDTH, y))

def end_game():
    print("Game Over")
    sys.exit()

def game_loop():
    running = True
    player_snake = Snake()
    apple = Food()
    movement_x, movement_y = 0, 0
    last_direction = None
    player_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                direction_keys = {pygame.K_UP: ('up', 0, -1), pygame.K_DOWN: ('down', 0, 1), pygame.K_RIGHT: ('right', 1, 0), pygame.K_LEFT: ('left', -1, 0)}
                if event.key in direction_keys and last_direction != direction_keys[event.key][0]:
                    last_direction, movement_x, movement_y = direction_keys[event.key]

        player_snake.update_position(movement_x, movement_y)

        if player_snake.detect_food_collision(apple):
            player_score += 1
            apple.respawn(player_snake.segments)
            player_snake.segments.append(player_snake.segments[-1])

        DISPLAY.fill(COLOR_BLACK)
        display_score = game_font.render(f'Score: {player_score}', True, COLOR_WHITE)
        DISPLAY.blit(display_score, (0, SCREEN_HEIGHT))
        player_snake.render()
        apple.draw()
        draw_playing_area()

        pygame.display.flip()
        game_clock.tick(10)

if __name__ == '__main__':
    game_loop()
