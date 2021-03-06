import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """背景星星图片"""
    def __init__(self, ai_game):
        """初始化星星"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
