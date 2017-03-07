from forecastiopy import *
from keys import DARK_SKY_KEY

Lisbon = [38.7252993, -9.1500364]

fio = ForecastIO.ForecastIO(DARK_SKY_KEY, latitude=Lisbon[0], longitude=Lisbon[1])
current = FIOCurrently.FIOCurrently(fio)
print('Temperature:', current.temperature)
print('Precipitation Probability:', current.precipProbability)
