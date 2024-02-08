import tkinter as tk
import logging
from tradingBot.connectors.binance_futures import BinanceFuturesClient
from tradingBot.connectors.bitmax import BitmexClient


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

    binance = BinanceFuturesClient("732655e0d3090c971a2166144d9bb8eeee397d49087f26ba4342045a796c385d",
                                   "4f81ce9435301a543061a9925e3d3872e3969b9387f6974efdf2516c3ccffc0d",
                                   True)

    bitmex = BitmexClient("t4aaDq4H0AMgin1qUs8Jm0gu", "YVQKHJveG1nAkLCCgWcw61Zn-VcLTI9ZE-hfSszuZUm7irOf", True)

    #print(bitmex.place_order(bitmex.contracts['XBTUSD'], "Limit", 50, "Buy", price=20000, tif="GoodTillCancel"))
    root = tk.Tk()

    root.mainloop()
