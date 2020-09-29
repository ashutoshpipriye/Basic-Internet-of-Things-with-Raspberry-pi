import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM);
GPIO.setup(19, GPIO.IN)


while True:
    input_value = GPIO.input(19)
    print str(input_value)