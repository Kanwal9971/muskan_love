import os,sys
from time import sleep
import multiprocessing
import threading


r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"




os.system("clear")
sleep(1.0)
def banner():
    print(w+d+"      ,,                ,,")
    print(w+d+"    (((((              )))))")
    print(w+d+"   ((((((              ))))))")
    print(w+d+"   ((((((              ))))))")
    print(w+d+"    ((((("+w+b+",r@@@@@@@@@@e,"+w+d+")))))")
    print(w+d+"      ((("+w+b+"@@@@@@@@@@@@@@@@"+w+d+")))    "+w+b+"Nitin-Muskan")
    print(w+b+"      \@@/"+r+",:::,"+w+b+"\/"+r+",:::,"+w+b+"\@@       "+w+"------------------")
    print(w+b+"     /@@@|"+r+":::::"+w+b+"||"+r+":::::"+w+b+"|@@@\\     "+r+"Instagram"+w+" : "+y+"@muskanverma906")
    print(w+b+"    / @@@\\"+r+"':::'"+w+b+"/\\"+r+"':::'"+w+b+"/@@@ \\    "+w)
    print(w+b+"   /  /@@@@@@@//\\\@@@@@@@\  \\   "+g+"I love you muskan")
    print(w+b+"  (  /  '@@@@@====@@@@@'  \  )  "+g+"mei amesha pyaar kartah rahunga")
    print(w+b+"   \(     /          \     )/   "+g+"Kesa laga suprise")
    print(w+b+"     \   (            )   /")
    print(w+b+"          \          /"+w)
banner()
print("\n")
print(r+"└─"+w+"\033[1;37m["+r+" 1"+w+" ] "+g+"Your gift"+w+" : ")
print(r+"└─"+w+"\033[1;37m["+r+" 2"+w+" ] "+g+"My Love"+w+" : ")
opp=int(input(r+"└─"+b+"\033[1;37mEnter Desire Option: "+r))

if opp==1:
    os.system("clear")
    banner()
    os.system("am start -a android.intent.action.VIEW -d https://kanwal9971.github.io/muskan-verma/ > /dev/null 2>&1 &")
    os.system("python3 mainsq.py")

if opp==2:
    os.system("clear")
    banner()
    print("\n")
    a = (r+"└─"+w+"\033[1;37m["+r+" ->"+w+" ] "+g+''' hum jub first time mila thay to mena ap ko whatsaap pa message kia tha❤️ 
    yr vo din first time mena kisi ladki sa 30 min baat ki 
    thi or us din sa la kr aaj tak hum ko 10 month ho ga🌹 
    wish you a very happy birthday dear muskan verma my heart❤️
    i am really thank full because tum na mera bhaut sath dia ha her time bhaut gussa
    kr ta tha bhaut log bhi aya bich ma but koi ni❤️ 
    fir bhi love you and sorry jyda persan kr ta hu nibbi (MUSKAN verma cute girl❤️ :) 
    )Happy birthday AgAiN🎂❤️🌹💐 '''+w+" : ")
    for i in a:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.1)
    print("\n")
    sleep(3.0)
    sys.exit