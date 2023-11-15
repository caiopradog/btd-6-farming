from utils import go_to_map, select_gamemode, click, convert_to_abs_coordinates, await_for_text
import time
from config import names, coordinates
from tower import Tower


def farm():
    go_to_map('Infernal')
    select_gamemode('Deflation')
    await_for_text(835, 365, 1080, 420, 'DEFLATION')
    click(coordinates.DEFLATION_OK_BUTTON)  # Click continue
    time.sleep(0.5)
    Tower("Discount Village", names.MONKEY_VILLAGE, convert_to_abs_coordinates((865, 326)), "202")
    Tower("Hero", names.HERO, convert_to_abs_coordinates((1007, 315)))
    Tower("Super 1", names.SUPER_MONKEY, convert_to_abs_coordinates((1007, 425)), "203")
    Tower("First Ninja", names.NINJA_MONKEY, convert_to_abs_coordinates((912, 436)), "402")
    Tower("Second Ninja", names.NINJA_MONKEY, convert_to_abs_coordinates((831, 436)), "402")
