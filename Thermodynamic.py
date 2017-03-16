# THERMODYNAMIC
# An installation art piece

# Gaby Clarke, Spring 2017
# Parsons Paris, Art Media and Technology Core Spatial Studio
# https://github.com/gabyclarke/Thermodynamic

# Powered by Dark Sky, https://darksky.net/poweredby/
# Powered by forecast.io Python3 wrapper,
# https://github.com/bitpixdigital/forecastiopy3

from threading import Timer
import serial
from forecastiopy import *
from keys import DARK_SKY_KEY

s = serial.Serial('/dev/cu.usbmodem1411', 9600)

# PARAMETERS TO BE EDITED
SanDiego = ["SanDiego",32.7157, 117.1611]
checkFrequency = 45.0

def sendTemperature(place, frequency):
    """ Checks the temperature at a position with a given frequency, then sends
        value to serial port.

        Inputs:
        place = [name, latitude, longitude] of a place (string, float, float)
        frequency = frequency of function call

        Output:
        sends value to serial port specified
    """
    Timer(frequency, sendTemperature, args=[place,frequency]).start()
    temperature = getCurrentTemp(place)
    temperature = str(temperature)
    s.write(temperature.encode())

def getCurrentTemp(place):
    """ Uses forecastiopy to get the current temperature at a position.

        Inputs:
        place = [latitude, longitude] of a place (type = list)

        Returns:
        current temperature (type = float)
    """
    FIO = ForecastIO.ForecastIO(DARK_SKY_KEY, latitude=place[1], longitude=place[2])
    current = FIOCurrently.FIOCurrently(FIO)
    return current.temperature

def run():
    sendTemperature(SanDiego, checkFrequency)

run()
