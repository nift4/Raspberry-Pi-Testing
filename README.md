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
A button test: Button #22 is used to display a image.
Sorry that I don't given that images to you ;)
```
sudo python3 test.py
```

## Requirements
evdev from pip3: "sudo pip3 install evdev"

pygame from apt: "sudo apt install python3-pygame"

pigame (with pigameui):
```
OLDDIR=`pwd`
TMPDIR=`mktemp`
cd $TMPDIR
wget https://github.com/n4archive/pigamedrv.github.io/raw/master/userdoc/installer.bin
bash installer.bin
cd $OLDDIR
rm -rdf $TMPDIR
```
