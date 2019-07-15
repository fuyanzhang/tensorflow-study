import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

# def go():
#     GPIO.setup(33,GPIO.OUT)
#     GPIO.setup(11,GPIO.OUT)
#     GPIO.setup(12,GPIO.OUT)
#     GPIO.output(33,True)
#     GPIO.output(11,True)
#     GPIO.output(12,False)

# def changeSpeed():
#     ENA = 33
#     leftpwm = GPIO.PWM(ENA, 50)
#     leftpwm.stop()
#     leftpwm.start(100)
#     leftpwm.ChangeDutyCycle(50)
def up():
    GPIO.output(11,True)
    GPIO.output(13,True)
    GPIO.output(15,False)
    GPIO.output(12,True)
    GPIO.output(16,True)
    GPIO.output(18,False)
        
up()
time.sleep(10)
# changeSpeed()
# time.sleep(5)
GPIO.cleanup()
