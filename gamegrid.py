# Python file to make the game grid
# Go to astar.py to see the program 
# This was created just to learn how to use pygame

import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
MAUVE = (224, 176, 255)  # colour tuples to be used later in the program
clock = pygame.time.Clock()

maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def windowLoop(maze):

    dim = len(maze)
    width = 32 * dim
    display = pygame.display.set_mode((width, width))
    display.fill(WHITE)  # fill the display with WHITE color

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()     
                sys.exit(0)
            for i in range(0, width, 32):
                pygame.draw.line(display, BLACK, (i, 0), (i, width))  # drawing row lines 32px apart
            for j in range(0, width, 32):
                # drawing column lines 32px apart
                pygame.draw.line(display, BLACK, (0, j), (width, j))
            pygame.display.update()

            for i in range(0, width, 32):
                # to deal with internal PyGame events in the event queue which cause the
                # system to freeze
                pygame.event.pump()
                for j in range(0, width, 32):
                    if maze[int(i/32)][int(j/32)] == 1:
                        pygame.draw.rect(display, BLACK, (j, i, 32, 32))
            pygame.display.update()




windowLoop(maze)
