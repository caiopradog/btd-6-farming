import win32gui
import re


class WindowManager:
    """encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def get_window_data(self):
        """get position and size of the window"""
        rect = win32gui.GetWindowRect(self._handle)
        x = rect[0]
        y = rect[1]
        width = rect[2] - x
        height = rect[3] - y

        return {"x": x, "y": y, "width": width, "height": height}
