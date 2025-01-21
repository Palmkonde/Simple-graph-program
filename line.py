import pygame
import logging

WIDTH = 600
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plotting line")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Program started")

def f(x: int) -> int:
    return x


if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        screen.fill((0, 0, 0))
        
        for x in range(WIDTH):
            x_position = x 
            y = WIDTH - f(x_position) 
            
            logger.info("x: %s, y:%s", x_position, y)
            screen.set_at((x_position ,y), (255, 255, 255))

        pygame.display.flip()                
    
    pygame.quit()
