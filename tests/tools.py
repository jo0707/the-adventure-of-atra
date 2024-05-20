import pygame

import constants
from src.utils.fontHelper import FontHelper
from src.utils.soundHelper import SoundHelper

already_set_up = False

def minimal_setup_for_game():
    global already_set_up
    if already_set_up:
        return
    pygame.init()
    FontHelper.initFonts()
    SoundHelper.initSounds()

    pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    already_set_up = True