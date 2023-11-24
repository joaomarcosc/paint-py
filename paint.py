import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
MIN_DRAW_SIZE, MAX_DRAW_SIZE = 1, 20
DRAW_SIZE = 5

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aplicação Paint")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BACKGROUND_COLOR)

draw_color = BLACK
draw_size = DRAW_SIZE

font = pygame.font.Font(None, 36)

drawing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(canvas, draw_color, pos, draw_size)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                draw_color = RED
            elif event.key == pygame.K_g:
                draw_color = GREEN
            elif event.key == pygame.K_b:
                draw_color = BLUE
            elif event.key == pygame.K_y:
                draw_color = YELLOW
            elif event.key == pygame.K_w:
                draw_color = WHITE
            elif event.key == pygame.K_UP:
                draw_size = min(MAX_DRAW_SIZE, draw_size + 1)
            elif event.key == pygame.K_DOWN:
                draw_size = max(MIN_DRAW_SIZE, draw_size - 1)

    screen.blit(canvas, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
