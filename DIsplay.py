import time
import imageio
import numpy as np
from FourByOneDisplay import FourByOneDisplay
from ConfigData import ConfigData
from PIL import Image


class Display(ConfigData):
    def __init__(self, surface):
        super().__init__()
        self.digits = self.HEIGHT * self.WIDTH
        self.MAX_NUMBER = 10 ** self.digits - 1
        self.displays = tuple(tuple(FourByOneDisplay(surface, i * self.MINI_WIDTH, j * self.MINI_HEIGHT)
                                    for i in range(self.WIDTH // 4))
                              for j in range(self.HEIGHT))
        self.number = -1
        if self.digits > 640:
            sys.set_int_max_str_digits(self.digits)
        self.resolution = (len(self.displays[0]) * 4 * 4, len(self.displays) * 6)
        self.live = {(0, 1): "a", (1, 0): "f", (1, 2): "b", (2, 1): "g", (3, 0): "e", (3, 2): "c", (4, 1): "d"}

    def get_pos(self, i, j):
        row = i // 6
        rel_i = i - 6 * row
        pad = j // 16
        digit = (j - 16 * pad) // 4
        rel_j = j - 16 * pad - 4 * digit
        return row, pad, digit, self.live[(rel_i, rel_j)]

    def call_digit(self, n):
        if n >= self.digits:
            raise ValueError(f"No digit found with number {n}")
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

    def load_image_path(self, path: str):
        img = Image.open(path).convert("L").resize(self.resolution)
        img.save("BWimg.png")
        img = np.array(img)
        self.load_image(img)

    def next_live_pixel(self, i, j):
        x = i % 6
        if x in [0, 2]:
            if j + 4 < self.resolution[0]:
                j += 4
            else:
                i += 1
                j = 0
        elif x == 4:
            if j + 4 < self.resolution[0]:
                j += 4
            else:
                i += 2
                j = 1
        elif x in [1, 3]:
            if j + 2 < self.resolution[0]:
                j += 2
            else:
                i += 1
                j = 1
        return i, j

    def load_image(self, img: np.array):
        i, j = 0, 1
        while i < self.resolution[1] and j < self.resolution[0]:
            n = self.get_pos(i, j)
            self.displays[n[0]][n[1]].displays[n[2]].draw_segment(i = n[3], lum = 255 - img[i, j])
            i, j = self.next_live_pixel(i, j)

    def load_video(self, video_path):
        frames = []
        reader = imageio.get_reader(video_path)
        for frame in reader:
            img = np.array(frame)
            img = Image.fromarray(img).convert("L").resize(self.resolution)
            frames.append(np.array(img))
            #self.load_image(img=img)
        reader.close()
        return frames


if __name__ == "__main__":
    import pygame
    import sys
    import random

    pygame.init()
    WIDTH, HEIGHT = 1800, 900
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("full")

    display = Display(screen)
    #display.load_image_path("img_2.png")
    x = time.time()
    frames = display.load_video("rick.mp4")
    print(time.time() - x)
    #display.update_number(int("8" * display.digits))
    i = 0
    while True:
        display.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #number = random.randint(1, display.MAX_NUMBER)
        display.load_image(img=frames[i % len(frames)])
        #display.update_number(number)
        #display.call_digit(59).update_number(1)
        pygame.display.flip()
        i += 1
        pygame.time.delay(30)
