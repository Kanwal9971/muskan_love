# scripted by nitin

import os ,sys
import threading
from time import sleep
import multiprocessing

# ----- colors 
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
#-----------

def banner():
    print(w+r+'''
_____$$$$_________$$$$
___$$$$$$$$_____$$$$$$$$
_$$$$$$$$$$$$_$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$$$$$$$$$
__$$$$$$$$$$$$$$$$$$$$$$$
____$$$$$$$$$$$$$$$$$$$
_______$$$$$$$$$$$$$
__________$$$$$$$
____________$$$
_____________$   
    ''')

class Muskan:
    define = '_data_main'
    def __init__(self):
        os.system("clear")
        banner()
        print("\n")
        print(r+"└─"+w+"\033[1;37m["+r+" --> "+w+" ] "+g+"I LOVE YOU MUSKAN"+w+" : ")
        sleep(3.0)
        os.system("clear")
        os.system("python3 password.py")

samay = Muskan()
