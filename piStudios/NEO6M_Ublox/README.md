## Interfacing NEO6M V2 GPS with Raspi

After interfacing as indicaated above, will decode the GPS data from [NMEA](https://www.gpsworld.com/what-exactly-is-gps-nmea-dat) codes.

### Requirements
1. [Raspberry Pi 3 Model B+ BCM2837B0 SoC, IoT, PoE Enabled]()
2. [U-blox NEO-6M GPS Module with EPROM]()
3. [Raspbian OS]()
4. [Jumper Cables]()
5. [Bread Board]()
### Steps



Hook up your pi and the NEO as shown in the diagram below.

- Connect `vcc` of GPS module to Power Supply (5V) of Raspberry Pi.
- Connect `Tx` (Transmitter Pin) of GPS module to any Raspberry Pi GPIO
- Connect `GND` (Ground Pin) of GPS module to Pin No.6 Raspberry.


## References

1.[Hackster](https://www.hackster.io/)
2.[GPS World, National Marine Electronics Association](https://www.gpsworld.com/what-exactly-is-gps-nmea-data/)
3.
