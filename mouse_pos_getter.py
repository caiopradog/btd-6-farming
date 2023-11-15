from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from config import keybinds


last_selected_monkey = None


def on_click(x, y, button, pressed):
    global last_selected_monkey
    if pressed and last_selected_monkey is not None:
        print(last_selected_monkey, f'({x}, {y})')
        last_selected_monkey = None


def on_press(key):
    global last_selected_monkey
    key = str(key).replace("'", "")
    monkey = next((keybind['tower'] for keybind in keybinds.MONKEY_KEYBINDS if keybind['keybind'] == key), None)
    if monkey is None:
        return
    last_selected_monkey = monkey


if __name__ == '__main__':
    keyboard_listener = KeyboardListener(on_press=on_press)
    mouse_listener = MouseListener(on_click=on_click)

    keyboard_listener.start()
    mouse_listener.start()
    keyboard_listener.join()
    mouse_listener.join()
