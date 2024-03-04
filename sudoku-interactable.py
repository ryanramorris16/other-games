import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 700, 700
CELL_SIZE = 600 // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a 9x9 grid
grid = [[0 for _ in range(9)] for _ in range(9)]

# Function to draw the grid
def draw_grid():
    for i in range(0, 10):
        if i % 3 == 0:
            thickness = 2
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE + 50, 50), (i * CELL_SIZE + 50, CELL_SIZE * 9 + 50), thickness) # vertical lines
        pygame.draw.line(screen, BLACK, (50, i * CELL_SIZE + 50), (CELL_SIZE * 9 + 50, i * CELL_SIZE + 50), thickness)  # horizontal lines

# Function to draw the numbers in the grid
def draw_numbers():
    font = pygame.font.Font(None, 30)
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text = font.render(str(grid[i][j]), True, BLACK)
                screen.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 15))

# Function to draw new, solve, and reset buttons
def draw_buttons():
    font = pygame.font.Font(None, 30)
    text = font.render("Reset", True, BLACK)
    screen.blit(text, (WIDTH // 2 + 175, HEIGHT - 40))
    
    text = font.render("Solve", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 25, HEIGHT - 40))
    
    text = font.render("New", True, BLACK)
    screen.blit(text, (WIDTH // 2 - 225, HEIGHT - 40))
    
# Function to reset the grid
def reset_grid():
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] > HEIGHT - 40 and pos[0] > WIDTH // 2 + 175 and pos[0] < WIDTH // 2 + 225:
                reset_grid()
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                pos = pygame.mouse.get_pos()
                i = pos[1] // CELL_SIZE
                j = pos[0] // CELL_SIZE
                grid[i][j] = int(event.unicode)

    screen.fill(WHITE)
    draw_grid()
    draw_numbers()
    draw_buttons()
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
