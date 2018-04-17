# _*_ coding: utf-8 _*_
__date__ = '2018/4/17 下午6:55'
import pygame
import settings


class Ship(object):
    def __init__(self, ai_setting, screen):
        """初始化飞船并设置其位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        # 加载飞船图像并获得其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放置每艘飞船在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性 center 中存储小数
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.center < self.ai_setting.screen_width:
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left and self.center > 0:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
