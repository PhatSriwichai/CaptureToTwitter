# CaptureToTwitter

##Device
* Raspberry Pi
* usb webcam

## How to do.
* follow this https://embeddedsysthang.wordpress.com/2016/05/20/using-a-usb-webcam-by-rpi-and-tweet/
* sudo apt-get update
* sudo apt-get install git
* git clone https://github.com/PhatSriwichai/CaptureToTwitter.git
* cd CaptureToTwitter
* open file webCamButton.py
* edit 	CONSUMER_KEY 
		CONSUMER_SECRET 
		ACCESS_KEY
		ACCESS_SECRET
*connect switch to raspberry pi
	- button switch input1 to GPIO11 use capture
	- button switch input2 to GPIO13 use close capture system
* sudo python webCamButton.py

## Reference
* https://embeddedsysthang.wordpress.com/2016/05/20/using-a-usb-webcam-by-rpi-and-tweet/
* http://stackoverflow.com/questions/29673348/how-to-open-camera-with-pygame-in-windows