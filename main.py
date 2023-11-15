import pydirectinput as pyinput
import math
import time
import datetime
import pytesseract
from window_manager import WindowManager
from PIL import ImageGrab
from functools import partial
from config import coordinates
from utils import click, play, await_for_text, check_defeat, check_levelup, check_win
from farms import infernal_deflation

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
bloons_window = WindowManager()
bloons_window.find_window_wildcard("BloonsTD6")


if __name__ == '__main__':
    # amount_to_loop = 50
    bloons_window.set_foreground()
    total_time_start = int(time.perf_counter())
    # print('Farmando {} vezes'.format(amount_to_loop))
    print('Farmando infinitas vezes')
    i = 0
    while True:
        time_start = int(time.perf_counter())
        print('Começando {}ᵃ run'.format(i+1))
        pyinput.PAUSE = 0.2
        await_for_text(760, 980, 910, 1115, 'PLAY', False)
        click(coordinates.PLAY_BUTTON)
        infernal_deflation.farm()
        play(True)
        game_won = False
        game_lost = False
        while not game_won and not game_lost:
            game_won = check_win()
            game_lost = check_defeat()
            check_levelup()
        time_end = int(time.perf_counter())
        time_elapsed = time_end - time_start
        print('Tempo gasto na run: {}'.format(datetime.timedelta(seconds=time_elapsed)))
        pyinput.PAUSE = 0.2
        if game_won:
            click(coordinates.VICTORY_NEXT_BUTTON)
            time.sleep(0.5)

        click(coordinates.GAME_END_HOME_BUTTON)
        if game_lost:
            print('Derrota!')
            break
        i = i + 1

    total_time_end = int(time.perf_counter())
    total_time_elapsed = total_time_end - total_time_start
    print('Tempo gasto no farm: {}'.format(datetime.timedelta(seconds=total_time_elapsed)))