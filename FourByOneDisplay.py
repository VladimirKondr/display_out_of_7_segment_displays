import pygame
from SevenSegmentDisplay import SevenSegmentDisplay


class FourByOneDisplay:
    def __init__(self, surface, x = 0, y = 0, segment_width=10, segment_length=50, indent=20):
        # Константы
        self.SEGMENT_WIDTH = segment_width
        self.SEGMENT_LENGTH = segment_length

        self.surface = surface
        self.coords = (x, y)
        self.indent = indent
        self.width = 4 * segment_length + 3 * indent
        self.length = 2 * segment_length + 3 * segment_width
        self.displays = tuple(SevenSegmentDisplay(surface,
                                                  x + (segment_length + indent) * i,
                                                  y,
                                                  segment_width,
                                                  segment_length) for i in range(4))
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
