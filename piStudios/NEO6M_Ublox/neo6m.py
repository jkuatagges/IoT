import pynmea2
import string 
import serial
import time

getLocation = True

while getLocation: #run forever
    port = "/../../dev/ttyAMA0" #Nav to where NMEA was initiated(/)
    ser = serial.Serial(port,baudrate=9600,timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline() #readline from the serial connection

    #if newdata[0:6] == "$GPGGA, GPRMC":
    if newdata[0:6] == "$GPGLL":
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude = " +str(lat) + ", Longitude=" + str(lng)
        print(gps)
