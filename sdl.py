import pygame,pigame
from pygame.locals import *
import os
from time import sleep
#Colours
WHITE = (255,255,255)
os.putenv('SDL_VIDEODRV','fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV','dummy')
os.putenv('SDL_MOUSEDEV','/dev/null')
os.putenv('DISPLAY','')
    
pygame.init()
pitft = pigame.PiTft()
lcd = pygame.display.set_mode((320, 240))
lcd.fill((0,0,0))
pygame.display.update()
     
font_big = pygame.font.Font(None, 50)
      
touch_buttons = {'Shutdown':(80,60), 'Quit':(240,60), '17 off':(80,180), '4 off':(240,180)}
       
for k,v in touch_buttons.items():
    text_surface = font_big.render('%s'%k, True, WHITE)
    rect = text_surface.get_rect(center=v)
    lcd.blit(text_surface, rect)
                        
pygame.display.update()
try:
    while True:
        pitft.update()
        # Scan touchscreen events
        for event in pygame.event.get():
            if(event.type is MOUSEBUTTONDOWN):
                x,y = pygame.mouse.get_pos()
                print(x,y)
            elif(event.type is MOUSEBUTTONUP):
                x,y = pygame.mouse.get_pos()
                print(x,y)
                #Find which quarter of the screen we're in
                if y > 120:
                    if x < 160:
                        print("17off")
                    else:
                        print("4off")
                else:
                    if x < 160:
                        pygame.quit() ; import sys
                        os.system("sudo poweroff") ; sys.exit(0)
                    else:
                        pygame.quit()
                        import sys
                        sys.exit(0)
        sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    del(pitft)
