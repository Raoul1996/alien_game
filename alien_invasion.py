# _*_ coding: utf-8 _*_
__date__ = '2018/4/17 下午6:27'

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.captcha)
    ship = Ship(ai_setting,screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


if __name__ == '__main__':
    run_game()
