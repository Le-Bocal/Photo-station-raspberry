import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import subprocess
import time
import picamera
from datetime import datetime
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image, ImageEnhance
import os
import xlrd
from matplotlib import pyplot as plt

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
    
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:#si le bouton est pressé
        print("Button was pushed!")
        
        GPIO.output(LED_PIN, GPIO.HIGH)
        now = datetime.now()
         
        
        jpegFileName='/home/pi/'+ now.strftime("%Y%m%d_%H%M%S") + '.jpg'
        camera = picamera.PiCamera()
        camera.resolution = (1280, 720)
              
        print(jpegFileName)
        camera.capture(jpegFileName)
        
        time.sleep(1)
        camera.close()
        img = cv2.imread(jpegFileName)
        file = jpegFileName
        #define the alpha and beta 
        alpha =3.2 # contrast control
        beta = 10 # Brightness control

    
        myData="" # initialisation de la variable qui contiendra le contenu de qrcode
        # bloc permettant de lire d'extraire le contenu du QrCode
        for barcode in decode(img):
                    
            myData=barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
                        
        #ouvre dans une fenêtre l'image avec le qrcode
        cv2.imshow('Result',img)
        cv2.waitKey(0)
        cv2.waitKey(0)
        
        # eteindre la led    
        GPIO.output(LED_PIN, GPIO.LOW)
                        
        #permet d'accéder à la base de données
        workbook=xlrd.open_workbook('/home/pi/Documents/members-34_03062023.xls')
        worksheet = workbook.sheet_by_index(0)
        data = ""
        
        # si le qrcode n'est pas lisible
        if myData=="":
            # on crée l'image et le fichier texte pour inclure sur le dodoc
            ImgName="QrCodePasDétecté"+now.strftime("%Y%m%d_%H%M%S")+'.jpg'
            os.rename(jpegFileName,"/home/pi/Documents/dodoc2/capture/"+ImgName)
            textFileName = "QrCodePasDétecté" + now.strftime("%Y%m%d_%H%M%S")+'.jpg.txt'
            # on ecrit les métadonnées dans le fichier texte 
            f= open("/home/pi/Documents/dodoc2/capture/"+textFileName,"w+")
            f.write("date_created: "+now.strftime("%Y%m%d_%H%M%S\n"))
            f.write("----\n")
            f.write("date_modified: "+now.strftime("%Y%m%d_%H%M%S\n"))
            f.write("----\n")
            f.write("date_uploaded: "+now.strftime("%Y%m%d_%H%M%S\n"))
            f.write("----\n")
            f.write("media_filename: "+ImgName+"\n")
            f.write("----\n")
            f.write("type: image\n")
            f.write("----\n")
            f.write("fav: false\n")
            f.write("----\n")
            f.write("ratio: 0.5625\n")
            f.write("----\n")
            f.close()
        else:
            find = False;
            for x in range(1,int(worksheet.cell_value(0,28))): 
                # si le qrcode est trouvé dans la base
                if worksheet.cell_value(x,27)==myData: 
                    find=True
                    data=worksheet.cell_value(x,2)+worksheet.cell_value(x,3)
                    #on rennome l'image et le fichier texte avec le nom de l'adhérant
                    ImgName=data+now.strftime("%Y%m%d_%H%M%S")+'.jpg'
                    os.rename(jpegFileName,'/home/pi/Documents/dodoc2/capture/'+ImgName)
                    #subprocess.call(['sh', './prise-
                    textFileName = data+now.strftime("%Y%m%d_%H%M%S")+'.jpg.txt'
                    f= open("/home/pi/Documents/dodoc2/capture/"+textFileName,"w+")
                    f.write("date_created: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("date_modified: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("date_uploaded: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("media_filename: "+ImgName+"\n")
                    f.write("----\n")
                    f.write("type: image\n")
                    f.write("----\n")
                    f.write("fav: false\n")
                    f.write("----\n")
                    f.write("ratio: 0.5625\n")
                    f.write("----\n")
                    f.close()
                else:
                    data=worksheet.cell_value(x,2)+worksheet.cell_value(x,3)
                    ImgName=data+now.strftime("%Y%m%d_%H%M%S")+'.jpg'
                    os.rename(jpegFileName,'/home/pi/Documents/dodoc2/capture/'+ImgName)
                    #subprocess.call(['sh', './prise-
                    textFileName = data+now.strftime("%Y%m%d_%H%M%S")+'.jpg.txt'
                    f= open("/home/pi/Documents/dodoc2/capture/"+textFileName,"w+")
                    f.write("date_created: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("date_modified: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("date_uploaded: "+now.strftime("%Y%m%d_%H%M%S\n"))
                    f.write("----\n")
                    f.write("media_filename: "+ImgName+"\n")
                    f.write("----\n")
                    f.write("type: image\n")
                    f.write("----\n")
                    f.write("fav: false\n")
                    f.write("----\n")
                    f.write("ratio: 0.5625\n")
                    f.write("----\n")
                    f.close()
