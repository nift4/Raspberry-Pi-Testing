function runapp {
	PIGAME_SWAPXY=on PIGAME_INVERTY=on /usr/bin/python3 /home/pi/.pimenu/sdlkit.py
}
(/usr/bin/tvservice -s | /bin/egrep 'HDMI|DVI') || runapp
while :
do
	/usr/bin/python3 /home/pi/.pimenu/detectbtn.py
	runapp
done
