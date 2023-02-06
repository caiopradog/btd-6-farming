import pydirectinput as pyinput
import math
import time
import datetime
import pytesseract
from window_manager import WindowManager
from PIL import ImageGrab
from functools import partial
from config import keybinds, names, coordinates
from tower import Tower

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract.exe'
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
bloons_window = WindowManager()
bloons_window.find_window_wildcard("BloonsTD6")


def click(coords, clicks=1):
    abs_coords = convert_to_abs_coordinates(coords)
    pyinput.click(abs_coords[0], abs_coords[1], clicks=clicks)


def convert_to_abs_coordinates(coordinates):
    window_data = bloons_window.get_window_data()
    abs_coordinates = []
    for index, point in enumerate(list(coordinates)):
        axis = 'x' if index % 2 == 0 else 'y'
        abs_coordinates.append(point + window_data[axis])
    return tuple(abs_coordinates)


def read_coordinates(x1, y1, x2, y2, do_grayscale=True):
    absolute_coordinates = convert_to_abs_coordinates((x1, y1, x2, y2))
    image = ImageGrab.grab(bbox=absolute_coordinates)
    if do_grayscale:
        image = image.convert('L')
    return pytesseract.image_to_string(image, lang='eng')


def check_text(x1, y1, x2, y2, find_text, do_grayscale=True):
    text_in_game = read_coordinates(x1, y1, x2, y2, do_grayscale)
    text_found = find_text.upper() in text_in_game.upper()
    return text_found


def await_for_text(x1, y1, x2, y2, find_text, do_grayscale=True):
    text_found = False
    while not text_found:
        text_found = check_text(x1, y1, x2, y2, find_text, do_grayscale)


def check_win():
    text_in_game = read_coordinates(700, 120, 1215, 235)
    has_user_won = 'VICTORY' in text_in_game.upper()
    return has_user_won


def check_defeat():
    text_in_game = read_coordinates(705, 270, 1210, 420)
    # DEFCAT pq o OCR não consegue ler DEFEAT
    has_user_lost = 'DEFEAT' in text_in_game.upper() or 'DEFCAT' in text_in_game.upper()
    return has_user_lost


def check_levelup():
    text_in_game = read_coordinates(825, 540, 1090, 600)
    has_user_leveled_up = 'LEVEL UP' in text_in_game.upper()
    if has_user_leveled_up:
        print("Level Up!")
        click((810, 540))
        time.sleep(.5)
        click((810, 540))


def play(fast_forward):
    pyinput.press(keybinds.PLAY_FAST_FOWARD, presses=2 if fast_forward else 1)


def go_to_map(map):
    data = next(data for data in names.MAPS.items() if map in data[1])
    if not data:
        print("Map non existent")
    difficulty = data[0]
    maps = data[1]
    map_position = maps.index(map)
    map_page = math.floor(map_position / 6)
    map_position = maps.index(map) % 6
    click(coordinates.MAP_DIFFICULTIES[difficulty])
    if map_page != 0:
        click(coordinates.MAP_RIGHT_BUTTON, clicks=map_page)
    click(coordinates.MAPS[map_position])


def select_gamemode(game_mode):
    difficulty = next(data[0] for data in names.DIFFICULTIES.items() if game_mode in data[1])
    if not difficulty:
        print("Difficulty non existent")
    click(coordinates.GAME_DIFFICULTIES[difficulty])
    click(coordinates.GAME_MODES[game_mode])


def dark_castle_deflation():
    go_to_map('Dark Castle')
    select_gamemode('Deflation')
    await_for_text(835, 365, 1080, 420, 'DEFLATION')
    click(coordinates.DEFLATION_OK_BUTTON)  # Click continue
    time.sleep(0.5)
    Tower("Discount Village", names.MONKEY_VILLAGE, convert_to_abs_coordinates((865, 326)), "202")
    Tower("Hero", names.HERO, convert_to_abs_coordinates((1007, 315)))
    Tower("Super 1", names.SUPER_MONKEY, convert_to_abs_coordinates((1007, 425)), "203")
    Tower("First Ninja", names.NINJA_MONKEY, convert_to_abs_coordinates((912, 436)), "402")
    Tower("Second Ninja", names.NINJA_MONKEY, convert_to_abs_coordinates((831, 436)), "402")


def infernal_deflation_2x_money():
    go_to_map('Infernal')
    select_gamemode('Deflation')
    await_for_text(835, 365, 1080, 420, 'DEFLATION')
    click(coordinates.DEFLATION_OK_BUTTON)  # Click continue
    time.sleep(0.5)
    Tower("Elite Defender", names.SNIPER_MONKEY, convert_to_abs_coordinates((1606, 473)), "205")
    Tower("Stronger Stimulant", names.ALCHEMIST, convert_to_abs_coordinates((1578, 545)), "420")
    Tower("MIB", names.MONKEY_VILLAGE, convert_to_abs_coordinates((1561, 625)), "230")


def infernal_deflation():
    go_to_map('Infernal')
    select_gamemode('Deflation')
    await_for_text(835, 365, 1080, 420, 'DEFLATION')
    click(coordinates.DEFLATION_OK_BUTTON)  # Click continue
    time.sleep(0.5)
    Tower("Discount", names.MONKEY_VILLAGE, convert_to_abs_coordinates((1561, 625)), "202")
    Tower("Elite Defender", names.SNIPER_MONKEY, convert_to_abs_coordinates((1606, 473)), "025")
    Tower("Stronger Stimulant", names.ALCHEMIST, convert_to_abs_coordinates((1578, 545)), "420")


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
        pyinput.PAUSE = 0.1
        await_for_text(760, 980, 910, 1115, 'PLAY', False)
        click(coordinates.PLAY_BUTTON)
        infernal_deflation()
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