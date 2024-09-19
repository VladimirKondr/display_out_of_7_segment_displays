class ConfigData:
    def __init__(self, segment_length=25 / 5, segment_width=5 / 5, inner_indent = 10 / 5, outer_indent = 10 / 5, width = 512, height = 128):
        assert width % 4 == 0
        import pygame
        self.pygame = pygame
        self.SEGMENT_WIDTH = segment_width
        self.SEGMENT_LENGTH = segment_length
        self.INNER_INDENT = inner_indent
        self.OUTER_INDENT = outer_indent
        self.WIDTH = width
        self.HEIGHT = height
        self.calculate()

    def calculate(self):
        self.MINI_WIDTH = 4 * self.SEGMENT_LENGTH + 3 * self.INNER_INDENT + self.OUTER_INDENT
        self.MINI_HEIGHT = 3 * self.SEGMENT_WIDTH + 2 * self.SEGMENT_LENGTH + self.OUTER_INDENT


