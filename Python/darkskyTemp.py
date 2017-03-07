from keys import DARK_SKY_KEY
from forecastiopy import *

SanDiego = [32.7157, 117.1611]

def writeFile(data):
    """ Writes data to text file, with each entry on a new line.
        Input:
        data (type = float, converted to string)
    """
    f = open("temperatures.txt", 'a')
    f.write(str(data)+"\n")
    f.close
    
def getCurrentTemp(place):
    """ Uses forecastiopy to get the current temperature at a position.

        Inputs:
        place = [latitude, longitude] of a place (type = list)

        Returns:
        current temperature (type = float)
    """
    FIO = ForecastIO.ForecastIO(DARK_SKY_KEY, latitude=place[0], longitude=place[1])
    current = FIOCurrently.FIOCurrently(FIO)
    return current.temperature

def run():
    temperature = getCurrentTemp(SanDiego)
    writeFile(temperature)

run()
