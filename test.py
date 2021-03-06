from pigame import PiTft
import os, sys
pitft=PiTft()
try:
    while True:
        if pitft.Button1:
            os.system("sudo fbi -T 2 -a -noverbose -d /dev/fb1 ~pi/adapiluv320x240.jpg; sleep 2; sudo pkill fbi")
        if pitft.Button2:
            pass
        if pitft.Button3:
            pass
        if pitft.Button4:
            pass
except KeyboardInterrupt:
    del(pitft)
    sys.exit(0)
