#microSPOT | BBC microBit Spotify Controller by M.Argyle 11/26/18
import serial
import os
import time
from subprocess import call
playbackStatus = 0
shuffleStatus = 0
os.system("spotify stop") 
# Open serial port to listen. You may need to edit tty addßress. 
# Enter ls /tty.usb* in terminal after plugging button board in to 
# find correct address
serialPort = serial.Serial("/dev/cu.usbmodem1412", 115200, timeout=0.5)
print "microSPOT is listening"
#listen for button, button sends single string over serial to trigger
while True:    
    command = serialPort.read()
    #play/pause loop
    if command == "p":
        if playbackStatus == 0:
            os.system("spotify play")  
            playbackStatus = 1 
        else:
            os.system("spotify stop")
            playbackStatus = 0
    #next song loop        
    if command == ">":
       os.system("spotify next")
    #shuffle on off loop††å
    if command == "s":
        if shuffleStatus == 0:
            os.system("spotify toggle shuffle")
            os.system("spotify next")
            shuffleStatus = 1
        else:
            os.system("spotify toggle shuffle")
            shuffleStatus = 0
    #volume down
    if command == "-":
        os.system("spotify vol down")
    #volume up
    if command == "+":
        os.system("spotify vol up")
    #super special song, edit to your liking
    if command == "!":
        os.system("spotify play walking on sunshine")






      



