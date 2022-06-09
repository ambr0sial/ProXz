#ProXz
import time
import colorama
from colorama import Fore, Back, Style, init
from core.freeprx import freeprx

colorama.init()

def pb():
	tm = 2
	text2 =  Fore.YELLOW + "{}"
	t = time.monotonic()
	while time.monotonic() - t < tm:
		print(text2.format('\033[36mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[31mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[32mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[36mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[33mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[34mProcessing...') + '\r', end='')
		time.sleep(.08)
		print(text2.format('\033[35mProcessing...') + '\r', end='')
		time.sleep(.08)

input("Press [ENTER] to generate free proxies. These proxies will be saved at ./proxies.txt")
pb()
freeprx()
input("Generated successfully!")