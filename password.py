#
#
#
import os
import sys
from time import sleep
#
#
#------------------------

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"

#--------------------------

def banner3():
    os.system("clear")
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
    sleep(1.0)


def banner2():
    os.system("clear")
    print(w+b+'''____$$$$$$$$$
___$__$$$$$__$
__$__$$___$$__$
_$___$$________$
__$___$$$$____$
___$_____$$__$
____$_$$_$$_$
_____$_$$$_$
______$___$
_______$_$
________$
''')

banner2()

encrypt = "nitinwedsneha"

for enc in range(3):
    vrushabh = input(r+"└─"+b+"\033[1;37mEnter Password : "+r)
    if encrypt==vrushabh:
        samay = True
        os.system("clear")
        banner3()
        print(r+"└─"+b+"\033[1;37mCongratulations Password is Correct ! "+r)
        sleep(3.0)
        os.system("python3 mainsq.py")
        break    
    else:
       print("\n")
       print(r+"└─"+g+"\033[1;37mIncorrect Password ! Dare complete karo !  "+r)
       sys.exit
        

        
 

        
        


    



