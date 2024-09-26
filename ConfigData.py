class ConfigData:
    def __init__(self, segment_length=25, segment_width=5, inner_indent = 15, outer_indent = 15, coef = 3, width = 12, height = 17):
        assert width % 4 == 0
        import pygame
        self.pygame = pygame
        self.COEF = coef
        self.SEGMENT_WIDTH = segment_width / self.COEF
        self.SEGMENT_LENGTH = segment_length / self.COEF
        self.INNER_INDENT = inner_indent / self.COEF
        self.OUTER_INDENT = outer_indent /  self.COEF
        self.WIDTH = width
        self.HEIGHT = height
        self.calculate()

    def calculate(self):
        self.MINI_WIDTH = 4 * self.SEGMENT_LENGTH + 3 * self.INNER_INDENT + self.OUTER_INDENT
        self.MINI_HEIGHT = 3 * self.SEGMENT_WIDTH + 2 * self.SEGMENT_LENGTH + self.OUTER_INDENT


