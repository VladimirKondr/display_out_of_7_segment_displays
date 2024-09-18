class ConfigData:
    def __init__(self, segment_length=50, segment_width=10, inner_indent = 20):
        import pygame
        self.pygame = pygame
        self.SEGMENT_WIDTH = segment_width
        self.SEGMENT_LENGTH = segment_length
        self.INNER_INDENT = inner_indent

