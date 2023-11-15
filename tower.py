import pydirectinput as pyinput
from config import keybinds, names


class Tower:
    def __init__(self, name, tower, coords, level="000"):
        pyinput.PAUSE = 0.025
        self.name = name
        self.tower = tower
        self.x = coords[0]
        self.y = coords[1]
        self.level = level
        self.upgrades = {names.TOP_PATH: 0, names.MIDDLE_PATH: 0, names.BOTTOM_PATH: 0}
        pyinput.moveTo(self.x, self.y)
        pyinput.press(self.get_tower_keybind())
        pyinput.click()
        if level != "000":
            self.set_tier(level)

    def get_tower_keybind(self):
        return next(keybind["keybind"] for keybind in keybinds.MONKEY_KEYBINDS if keybind['tower'] == self.tower)

    def set_tier(self, level):
        pyinput.PAUSE = 0.025
        pyinput.click(self.x, self.y)
        paths = [names.TOP_PATH, names.MIDDLE_PATH, names.BOTTOM_PATH]
        for path, tier in enumerate(level):
            self.upgrade(paths[path], tier)
        self.level = level
        pyinput.press('esc')

    def upgrade(self, path, level):
        pyinput.PAUSE = 0.025
        presses = int(level) - int(self.upgrades[path])
        pyinput.press(keybinds.UPGRADE_KEYBINDS[path], presses=presses)
        self.upgrades[path] = level

    def ugrade_hero(self, levels):
        pyinput.click(self.x, self.y)
        pyinput.press(keybinds.UPGRADE_TOP_PATH, presses=levels)
        pyinput.press('esc')
