import ctypes

def show_fake_alert():
    ctypes.windll.user32.MessageBoxW(
        0,
        "A critical system error occurred. Press OK to continue.",
        "System Alert",
        0x10
    )