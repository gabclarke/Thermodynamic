import pyowm
from keys import OPEN_WEATHER_MAP_KEY2

owm = pyowm.OWM(OPEN_WEATHER_MAP_KEY2)

observation = owm.weather_at_zip_code('92009', 'us')
w = observation.get_weather()
temp = w.get_temperature('farenheit')

print temp('temp')