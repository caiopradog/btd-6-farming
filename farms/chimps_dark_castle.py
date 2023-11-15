from utils import go_to_map, select_gamemode, click, convert_to_abs_coordinates
import time
from config import names
from tower import Tower

"""
Dart Monkey 1 (730, 661)
Monkey Sub 1 (1083, 690)

Dart Monkey 2 (681, 702)
Hero (876, 444)
Druid 1 (797, 439)
Druid 2 (950, 448)
Druid 3 (724, 421)

Monkey Sub 1 -> 200
Dart Monkey 1 -> 002
Monkey Sub 1 -> 203

Druid 4 (802, 370)
Druid 5 (910, 386)
420 Alchemist 1 (1016, 664)
Druid 6 (987, 380)
220 Monkey Village (875, 294)

Druids -> 014
420 Alchemist 2 (695, 364)
320 Alchemist 3 (762, 318)
Druid 1 -> 015

Monkey Village -> 230
Alchemist 3 -> 420

Spike Factory -> 025
024 Glue Gunner (713, 280)
420 Sniper Monkey (938, 232)
402 Ice Monkey (573, 483)"""
def dark_castle_chimps():
    go_to_map('Infernal')
    select_gamemode('Deflation')
    time.sleep(1)
    dart = Tower("Camo Dart", names.DART_MONKEY, convert_to_abs_coordinates((730, 661)))
    sub = Tower("Monkey Sub 1", names.MONKEY_SUB, convert_to_abs_coordinates((1083, 690)))
    Tower("Dart Monkey 2", names.DART_MONKEY, convert_to_abs_coordinates((681, 702)))
    Tower("Obyn", names.HERO, convert_to_abs_coordinates((876, 444)))
    "Fazer lógica para comprar upgrade somente se tiver o dinheiro"
    sub.set_tier('200')
    Tower("Sub Alchemist", names.ALCHEMIST, convert_to_abs_coordinates((1016, 664)), '420')
    dart.set_tier('002')
    sub.set_tier('203')
    druids = [
        Tower("Avatar of Wrath", names.DRUID, convert_to_abs_coordinates((797, 439))),
        Tower("Poplust 1", names.DRUID, convert_to_abs_coordinates((797, 439))),
        Tower("Poplust 2", names.DRUID, convert_to_abs_coordinates((950, 448))),
        Tower("Poplust 3", names.DRUID, convert_to_abs_coordinates((724, 421))),
        Tower("Poplust 4", names.DRUID, convert_to_abs_coordinates((802, 370))),
        Tower("Poplust 5", names.DRUID, convert_to_abs_coordinates((910, 386)))
    ]
    village = Tower('Druid Village', names.MONKEY_VILLAGE, convert_to_abs_coordinates((875, 294)))

    for druid in druids:
        druid.set_tier('013')

    for druid in druids:
        druid.set_tier('014')

    Tower("Druids Alchemist 1", names.ALCHEMIST, convert_to_abs_coordinates((695, 364)), "420")
    Tower("Druids Alchemist 2", names.ALCHEMIST, convert_to_abs_coordinates((762, 318)), "320")
    druids[0].set_tier('015')
    village.set_tier('024')
