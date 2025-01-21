import pygame
import logging
import math

WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plotting line")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")


def f(x: int) -> int:
    return math.sin(x)


x_prev = None
y_prev = None

min_x, max_x = -6, 6
min_y, max_y = 0, 4

scale_x = WIDTH/(max_x - min_x)
scale_y = HEIGHT/(max_y - min_y)

N = 1000  # number of point to draw

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill((0, 0, 0))

        for i in range(N):
            x = min_x + (max_x - min_x) * i/N
            y = f(x)
            plot_x = int((x - min_x) * scale_x)
            plot_y = (HEIGHT//2) - int((y - min_y) * scale_y)

            if x_prev != None:
                pygame.draw.line(screen,
                                 color=(255, 255, 255),
                                 start_pos=(x_prev, y_prev),
                                 end_pos=(plot_x, plot_y))

            x_prev = plot_x
            y_prev = plot_y
            logger.info("x_prev: %s, y_prev: %s, x: %s, y: %s",
                        x_prev, y_prev, plot_x, plot_y)

            if i == N-1:
                x_prev, y_prev = None, None

        # running = False

        pygame.display.flip()

    pygame.quit()

"""

"""
