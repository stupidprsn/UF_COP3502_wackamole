from random import randrange
from typing import Final

import pygame

NUM_COLOUMNS: Final[int] = 20
NUM_ROWS: Final[int] = 16
CELL_SIZE: Final[int] = 32

class Mole:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.image: pygame.Surface = pygame.image.load("mole.png")

    def newPosition(self):
        self.x = randrange(0, NUM_COLOUMNS - 1) * CELL_SIZE
        self.y = randrange(0, NUM_ROWS - 1) * CELL_SIZE

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        return screen.blit(self.image, self.image.get_rect(
            topleft=(self.x, self.y))
        )

def main():
    try:
        pygame.init()
        screen: pygame.surface = pygame.display.set_mode((640, 512))

        mole: Mole = Mole()

        clock: pygame.time.Clock = pygame.time.Clock()
        running: bool = True

        while running:

            drawGrid(screen)
            position: pygame.Rect = mole.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if position.collidepoint(event.pos):
                        mole.newPosition()

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


def drawGrid(screen: pygame.surface) -> None:
    screen.fill("light green")

    for i in range(NUM_COLOUMNS):
        x: int = i * CELL_SIZE
        pygame.draw.line(screen, "black", (x, 0), (x, 512), 1)
    for i in range(NUM_ROWS):
        y: int = i * CELL_SIZE
        pygame.draw.line(screen, "black", (0, y), (640, y), 1)


if __name__ == "__main__":
    main()
