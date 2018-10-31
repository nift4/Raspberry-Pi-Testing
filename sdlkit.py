import pygame
import os
import pygameui as ui
import logging

log_format = '%(asctime)-6s: %(name)s - %(levelname)s - %(message)s'
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format))
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'dummy')
os.putenv('SDL_MOUSEDEV', '/dev/null')
 
MARGIN = 20
 
class PiTft(ui.Scene):
    def __init__(self):
        ui.Scene.__init__(self)
 
        self.on17_button = ui.Button(ui.Rect(MARGIN, MARGIN, 130, 90), '17 on')
        self.on17_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.on17_button)
 
        self.on4_button = ui.Button(ui.Rect(170, MARGIN, 130, 90), '4 on')
        self.on4_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.on4_button)
 
        self.off17_button = ui.Button(ui.Rect(MARGIN, 130, 130, 90), '17 off')
        self.off17_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.off17_button)
 
        self.off4_button = ui.Button(ui.Rect(170, 130, 130, 90), '4 off')
        self.off4_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.off4_button)
 
    def gpi_button(self, btn, mbtn):
        logger.info(btn.text)
         
        if btn.text == '17 on':
            print("17 on")
        elif btn.text == '4 on':
            print("4 on")
        elif btn.text == '17 off':
            print("17 off")
        elif btn.text == '4 off':
            print("4 off")

ui.init('Raspberry Pi UI', (320, 240))
pygame.mouse.set_visible(True)
ui.scene.push(PiTft())
ui.run()
