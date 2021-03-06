import pigame
from time import sleep
pitft = pigame.PiTft()
quit = False
def btn1(ignored):
    global quit
    quit = True
pitft.Button1Interrupt(btn1)
while not quit:
    sleep(2)
del(pitft)
