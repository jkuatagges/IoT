import pynmea2
import string 
import serial
import time
import os

getLocation = True

def runNeo():
    while getLocation: 
        port = “/dev/ttyAMAO”
        ser = serial.Serial(port,baudrate=9600,timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline()
        
    print("Getting Latitude and Longitude")

    #if newdata[0:6] == “$GPGGA”:
    if newdata[0:6] == “$GPRMC”:
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = “Latitude = " +str(lat) + “and Longitude=" + str(lng)
        print(gps)
