import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
import time
import picamera
from datetime import datetime


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
BUTTON_PIN = 14
LED_PIN = 4
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.setup(LED_PIN, GPIO.OUT)




#GPIO.cleanup()
def textFileCreation():
    now = datetime.now()
    textFileName = now.strftime("%d/%m/%Y %H:%M:%S")


while True: # Run forever
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button was pushed!")
        #subprocess.run("cat './prise-photo-station.sh'", shell=True)
        GPIO.output(LED_PIN, GPIO.HIGH)
        now = datetime.now()
        #textFileName = now.strftime("%d/%m/%Y %H:%M:%S") + '.jpg.txt'
        textFileName = now.strftime("%Y%m%d_%H%M%S") + '.jpg.txt'
        jpegFileName='/home/pi/Documents/dodoc2/station-de-captation-photo/'+ now.strftime("%Y%m%d_%H%M%S") + '.jpg'
        f= open("/home/pi/Documents/dodoc2/station-de-captation-photo/"+textFileName,"w+")
        f.write("date_created: "+now.strftime("%Y%m%d_%H%M%S\n"))
        f.write("----\n")
        f.write("date_modified: "+now.strftime("%Y%m%d_%H%M%S\n"))
        f.write("----\n")
        f.write("date_uploaded: "+now.strftime("%Y%m%d_%H%M%S\n"))
        f.write("----\n")
        f.write("media_filename: "+now.strftime("%Y%m%d_%H%M%S") + '.jpg\n')
        f.write("----\n")
        f.write("type: image\n")
        f.write("----\n")
        f.write("fav: false\n")
        f.write("----\n")
        f.write("ratio: 0.5625\n")
        f.write("----\n")
        f.close()
        camera = picamera.PiCamera()
        
        print(jpegFileName)
        camera.capture(jpegFileName)
        #subprocess.call(['sh', './prise-photo-station.sh'])
        
        time.sleep(1)
        camera.close()
        
        GPIO.output(LED_PIN, GPIO.LOW)
        
        #GPIO.cleanup()
        