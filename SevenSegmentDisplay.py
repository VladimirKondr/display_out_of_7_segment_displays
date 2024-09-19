from ConfigData import ConfigData
class SevenSegmentDisplay(ConfigData):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self.dic = {0: "abcdef",
                    1: "bc",
                    2: "abged",
                    3: "abcdg",
                    4: "fgbc",
                    5: "afgcd",
                    6: "afgecd",
                    7: "abc",
                    8: "abcdefg",
                    9: "abcdfg"}
        self.coords = (x, y)
        self.segments = {x: False for x in "abcdefg"}
        self.surface = surface
        self.number = 0
        n = "afgedbc"
        rect_props = [[x, y, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH],
                      [x, y + self.SEGMENT_WIDTH, self.SEGMENT_WIDTH, self.SEGMENT_LENGTH],
                      [x, y + self.SEGMENT_WIDTH + self.SEGMENT_LENGTH, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH],
                      [x, y + self.SEGMENT_WIDTH + self.SEGMENT_LENGTH + self.SEGMENT_WIDTH, self.SEGMENT_WIDTH, self.SEGMENT_LENGTH],
                      [x, y + self.SEGMENT_WIDTH + self.SEGMENT_LENGTH + self.SEGMENT_WIDTH + self.SEGMENT_LENGTH, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH],
                      [x + self.SEGMENT_LENGTH - self.SEGMENT_WIDTH, y + self.SEGMENT_WIDTH, self.SEGMENT_WIDTH, self.SEGMENT_LENGTH],
                      [x + self.SEGMENT_LENGTH - self.SEGMENT_WIDTH, y + self.SEGMENT_WIDTH + self.SEGMENT_LENGTH + self.SEGMENT_WIDTH, self.SEGMENT_WIDTH, self.SEGMENT_LENGTH]]
        self.recs = {n[i]: self.pygame.rect.Rect(*rect_props[i]) for i in range(7)}

    def draw_segment(self, i, lum = 1):
        if not self.segments[i]:
            self.pygame.draw.rect(self.surface, color=(255 / (1 - lum) if lum != 1 else 255, 0, 0), rect=self.recs[i])
            self.segments[i] = True

    def undraw_segment(self, i):
        if self.segments[i]:
            self.pygame.draw.rect(self.surface, color=(0, 0, 0), rect=self.recs[i])
            self.segments[i] = False

    def clear(self):
        # self.surface.fill((0, 0, 0))
        for i in self.segments:
            self.undraw_segment(i)

    def draw_number(self):
        n = self.dic[self.number]
        for i in self.segments:
            if i in n:
                self.draw_segment(i)
            elif i not in n:
                self.undraw_segment(i)

    def update_number(self, number):
        self.number = number
        self.draw_number()


if __name__ == "__main__":
    import pygame
    import sys

    pygame.init()
    # Настройка окна
    WIDTH, HEIGHT = 300, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("7-Segment Display")

    # Создание дисплея
    display = SevenSegmentDisplay(screen)

    # Главный цикл
    number = 0
    n = "abcdefg"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #display.update_number(number)
        pygame.display.flip()

        number = (number + 1) % 10
        pygame.time.delay(1000)  # Задержка 1 секунда