from signal import signal, SIGTERM, SIGHUP, pause
from time import timeout
import pynmea2
import string 
import serial

def safe_exit(signum, frame):
    exit(1)
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:     
    getLocation = True
    while getLocation: #run forever
        port = "/../../dev/ttyAMA0" #Nav to where NMEA was initiated(/)
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata = ser.readline() #readline from the serial connection

        #if newdata[0:6] == "$GPGGA, GPRMC":
        if newdata[0:6] == "$GPGLL": #get GPsGlobal data as Lat, Long
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "Lat = " +str(lat) + ", Long =" + str(lng)
            print(gps)
            
except KeyboardInterrupt:
    pass

finally:
    pass

