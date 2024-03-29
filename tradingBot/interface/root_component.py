import tkinter as tk
from tradingBot.interface.styling import *
from tradingBot.interface.logging_component import Logging
import time


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trading Bot")
        self.configure(bg=BG_COLOR)

        self._left_frame = tk.Frame(self, bg=BG_COLOR)
        self._left_frame.pack(side=tk.LEFT)

        self._right_frame = tk.Frame(self, bg=BG_COLOR)
        self._right_frame.pack(side=tk.LEFT)

        self._logging_frame = Logging(self._left_frame, bg=BG_COLOR)
        self._logging_frame.pack(side=tk.TOP)

        self._logging_frame.add_log("this is a test message")
        time.sleep(2)
        self._logging_frame.add_log("this is another test message")



