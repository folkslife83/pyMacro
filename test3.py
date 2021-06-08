import ctypes, platform

Active_W = ctypes.windll.user32.GetDesktopWindow()
ctypes.windll.user32.SetWindowPos(Active_W,0,0,0,0,0,0x0002|0x0001)