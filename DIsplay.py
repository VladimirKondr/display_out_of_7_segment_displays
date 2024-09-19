from FourByOneDisplay import FourByOneDisplay
from ConfigData import ConfigData

class Display(ConfigData):
    def __init__(self, surface):
        super().__init__()
        self.digits = self.HEIGHT * self.WIDTH
        self.MAX_NUMBER = 10 ** self.digits - 1
        self.displays = tuple(tuple(FourByOneDisplay(surface, i * self.MINI_WIDTH, j * self.MINI_HEIGHT)
                                    for i in range(self.WIDTH // 4))
                              for j in range(self.HEIGHT))
        self.number = 0
        if self.digits > 640:
            sys.set_int_max_str_digits(self.digits)
    
    def call_digit(self, n):
        if n >= self.digits:
            raise Exception(f"No digit found with number {n}")
        row = n // self.WIDTH
        n -= row * self.WIDTH
        pad = n // 4
        dig = n - pad * 4
        return self.displays[row][pad].displays[dig]

    def clear(self):
        for row in self.displays:
            for unit in row:
                unit.clear()

    def draw_number(self):
        x = str(self.number)
        for i in range(self.digits):
            f = int(x[i - self.digits + len(x)]) if i > (self.digits - len(x) - 1) else 0
            t = self.call_digit(i)
            if t.number != f:
                t.update_number(f)

    def update_number(self, number):
        self.number = number
        self.draw_number()



if __name__ == "__main__":
    import pygame
    import sys
    import random

    pygame.init()
    WIDTH, HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("full")

    display = Display(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        number = random.randint(1, display.MAX_NUMBER)
        display.update_number(number)
        #display.call_digit(59).update_number(1)
        pygame.display.flip()

        pygame.time.delay(1)



