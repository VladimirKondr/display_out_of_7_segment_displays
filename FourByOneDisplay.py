from ConfigData import ConfigData
from SevenSegmentDisplay import SevenSegmentDisplay


class FourByOneDisplay(ConfigData):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self.surface = surface
        self.coords = (x, y)
        self.displays = tuple(SevenSegmentDisplay(surface,
                                                  x + (self.SEGMENT_LENGTH + self.INNER_INDENT) * i,
                                                  y) for i in range(4))
        self.number = 0

    def clear(self):
        for unit in self.displays:
            unit.clear()

    def draw_number(self):
        x = str(self.number)
        for i in range(4):
            f = int(x[i - 4 + len(x)]) if i > (4 - len(x) - 1) else 0
            if self.displays[i].number != f:
                self.displays[i].update_number(f)

    def update_number(self, number):
        self.number = number
        self.draw_number()


if __name__ == "__main__":
    import pygame
    import sys

    pygame.init()
    WIDTH, HEIGHT = 500, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("4by1")

    display = FourByOneDisplay(screen)

    number = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #display.update_number(number)
        pygame.display.flip()

        number = (number + 1) % 10_000
        pygame.time.delay(100)
