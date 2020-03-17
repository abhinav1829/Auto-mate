import pyowm

owm = pyowm.OWM('61cf9c73e72fb837f80c3e97ecd03a37')
report = owm.weather_at_place('Pune')
result = report.get_weather()
detailed_status = result.get_detailed_status()
temp = result.get_temperature(unit='celsius')
# weather_result = 'It is ' \
#                  + detailed_status + ' in Pune. The temperature is ' \
#                  + temp + ' degrees celsius'
print(temp)
