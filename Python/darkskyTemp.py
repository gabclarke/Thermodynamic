from keys import DARK_SKY_KEY
from forecastiopy import *
import threading


SanDiego = ["SanDiego",32.7157, 117.1611]
checkFrequency = 10.0

def checkTemperature(place, frequency):
    """ Checks the temperature at a position with a given frequency, then writes
        new value to a line of a text file.


    """
    threading.Timer(frequency, checkTemperature).start()
    temperature = getCurrentTemp(place)
    filename = str(place[0]) + ".txt"
    writeFile(filename, temperature)


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

def writeFile(file, data):
    """ Writes data to text file, with each entry on a new line.
        Input:
        data (type = float, converted to string)
    """
    f = open(file, 'a')
    f.write(str(data)+"\n")
    f.close

def run():
    # temperature = getCurrentTemp(SanDiego)
    # writeFile(temperature)
    checkTemperature(SanDiego, checkFrequency)

run()
