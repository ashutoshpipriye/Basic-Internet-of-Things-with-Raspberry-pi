import Adafruit_DHT
 
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio=17
 
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
  print('Failed to get reading. Try again!')