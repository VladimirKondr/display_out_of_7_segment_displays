from ConfigData import ConfigData
from SevenSegmentDisplay import SevenSegmentDisplay


class FourByOneDisplay(ConfigData):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self.surface = surface
        self.coords = (x, y)
        self.width = 4 * self.SEGMENT_LENGTH + 3 * self.INNER_INDENT
        self.length = 2 * self.SEGMENT_LENGTH + 3 * self.SEGMENT_WIDTH
        self.displays = tuple(SevenSegmentDisplay(surface,
                                                  x + (self.SEGMENT_LENGTH + self.INNER_INDENT) * i,
                                                  y) for i in range(4))
        self.number = 0
        for unit in self.displays:
            unit.update_number(0)
            unit.draw_number()

    def clear(self):
        for unit in self.displays:
            unit.clear()

    def draw_number(self):
        x = str(self.number)
        x = "0" * (4 - len(x)) + x
        for i in range(3, -1, -1):
            f = int(x[i])
            if self.displays[i].number != f:
                self.displays[i].update_number(f)
                self.displays[i].draw_number()

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

        display.update_number(number)
        pygame.display.flip()

        number = (number + 1) % 10_000
        pygame.time.delay(1)
