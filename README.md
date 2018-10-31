# Raspberry-Pi-Testing
My tests with my pi3 + AdaFruit pitft+ 2.8" capatitive
## Function
WARNING: It must be as root.
### sdlkit.py
Run pygameui :)!!
```
sudo python3 sdlkit.py
```
### sdl.py
A simple ui for log and shutdown.
```
sudo python3 sdl.py
```
### test.py
A button test: Button #22 and #23 are used to display images.
Sorry that I don't given that images to you ;)
```
sudo python3 test.py
```

## Requirements
"pitftscreen.py" from [my repo PiTFT_Screen](https://github.com/nift4/PiTFT_Screen) required for test.py

"pitft_touchscreen.py" from [my repo pitft_touchscreen](https://github.com/nift4/pitft_touchscreen) required for sdl.py and sdlkit.py

"pigame.py" from [my repo pigame](https://github.com/nift4/pigame) required for sdl.py and sdlkit.py

evdev from pip3: "sudo pip3 install evdev" required for sdl.py and sdlkit.py

pygame from apt: "sudo apt install python3-pygame" required for sdl.py and sdlkit.py

pigameui: required for sdlkit.py
```
git clone https://github.com/nift4/pigameui.git
cd pigameui
sudo python3 setup.py install
```
