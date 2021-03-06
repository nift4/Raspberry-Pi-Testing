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
os.putenv('DISPLAY','')
 
MARGIN = 20
 
class PiTft(ui.Scene):
    def __init__(self,a,b,c,d,e):
        ui.Scene.__init__(self)
        self.callback = e
 
        self.off_button = ui.Button(ui.Rect(MARGIN, MARGIN, 130, 90), a)
        self.off_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.off_button)
 
        self.quit_button = ui.Button(ui.Rect(170, MARGIN, 130, 90), b)
        self.quit_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.quit_button)
 
        self.x_button = ui.Button(ui.Rect(MARGIN, 130, 130, 90), c)
        self.x_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.x_button)
 
        self.menu_button = ui.Button(ui.Rect(170, 130, 130, 90), d)
        self.menu_button.on_clicked.connect(self.gpi_button)
        self.add_child(self.menu_button)

    def gpi_button(self, btn, mbtn):
        self.callback(self, btn, mbtn)
 
def boot_menu(scence, btn, mbtn):
        logger.info(btn.text)
         
        if btn.text == 'Quit':
            pygame.event.post(pygame.event.Event(pygame.QUIT))
        elif btn.text == 'Shutdown':
            os.system("sudo poweroff")
        elif btn.text == 'Reboot':
            os.system("sudo reboot")
        elif btn.text == 'Menu':
            ui.scene.push(PiTft("NULL","NULL","NULL","Back",hub))

def hub(scence, btn, mbtn):
        logger.info(btn.text)

        if btn.text == 'Back':
            ui.scene.push(PiTft("Shutdown","Reboot","Quit","Menu",boot_menu))
        elif btn.text == 'Shutdown':
            os.system("sudo poweroff")
        elif btn.text == 'Reboot':
            os.system("sudo reboot")
        elif btn.text == 'Menu':
            ui.scene.push(PiTft("NULL","NULL","NULL","Back",hub))


ui.init('Raspberry Pi UI', (320, 240))
pygame.mouse.set_visible(True)
ui.scene.push(PiTft("Shutdown","Reboot","Quit","Menu",boot_menu))
ui.run()
