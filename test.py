from pigame import PiTft
import os
pitft=PiTft()
try:
    while True:
        if pitft.Button1:
            os.system("sudo fbi -T 2 -a -noverbose -d /dev/fb1 ~pi/adapiluv320x240.jpg")
        if pitft.Button2:
            os.system("sudo fbi -T 2 -a -noverbose -d /dev/fb1 ~pi/s2c.gif")
        if pitft.Button3:
            pass
        if pitft.Button4:
            pass
except KeyboardInterrupt:
    print("bye")
