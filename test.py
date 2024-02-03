from tradingBot.connectors.binance_futures import BinanceFuturesClient
client = BinanceFuturesClient("732655e0d3090c971a2166144d9bb8eeee397d49087f26ba4342045a796c385d",
                              "4f81ce9435301a543061a9925e3d3872e3969b9387f6974efdf2516c3ccffc0d",
                              True)
import time
import win32api
gt = client.get_server_time()
tt=time.gmtime(int((gt["serverTime"])/1000))
win32api.SetSystemTime(tt[0],tt[1],0,tt[2],tt[3],tt[4],tt[5],0)