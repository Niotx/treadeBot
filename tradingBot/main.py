import tkinter as tk
import logging
from tradingBot.connectors.bitmax import get_contracts

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# logger.debug("This message is important only when debugging the program")
# logger.info("This message just shows basic information")
# logger.warning("This message is about something you should pay attention to")
# logger.error("This message helps to debug an error that occurred in your program")

if __name__ == '__main__':

    bitmax_contracts = get_contracts()

    root = tk.Tk()
    root.configure(bg="gray12")

    i = 0
    j = 0

    caliber_font = ("caliber", 11, "normal")

    for contract in bitmax_contracts:
        labal_widget = tk.Label(root, text=contract, bg="gray12", fg="steelBlue", width=13, font=caliber_font)
        labal_widget.grid(row=i, column=j)
        if i == 4:
            j += 1
            i = 0
        else:
            i += 1

    root.mainloop()