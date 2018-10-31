# Raspberry-Pi-Testing
My tests with my pi3 + AdaFruit pitft+ 2.8" capatitive
## Function
WARNING: It must be as root.
### sdl.py
A simple ui for log and shutdown.
```
sudo python3 sdl.py
```
### test.py
A button test: Button #22 and #23 are used to display images.
```
sudo python3 test.py
```

## Requirements
"pitftscreen.py" from [my repo PiTFT_Screen](https://github.com/nift4/PiTFT_Screen)

"pitft_touchscreen.py" from [my repo pitft_touchscreen](https://github.com/nift4/pitft_touchscreen)

"pigame.py" from [my repo pigame](https://github.com/nift4/pigame)

evdev from pip3: "sudo pip3 install evdev"

pygame from apt: "sudo apt install python3-pygame"