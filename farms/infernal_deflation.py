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
    Tower("Spectre", names.MONKEY_ACE, convert_to_abs_coordinates((1569, 534)), "205")
    Tower("MIB", names.MONKEY_VILLAGE, convert_to_abs_coordinates((1564, 630)), "230")
