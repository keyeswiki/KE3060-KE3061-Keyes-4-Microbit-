from microbit import *
from microbit import sleep, i2c
from PCA9685 import *
from servo import *

num1 = 60
num2 = 90
num3 = 60
num4 = 120

Left_Y = 0
Left_X = 0
Right_Y = 0
Right_B = 0
pin14.PULL_UP
pin15.PULL_DOWN
pin14.write_digital(1)
pin15.write_digital(0)

pwm = PCA9685.PCA9685(i2c)

pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')

s1 = Servos(i2c)

s2 = Servos(i2c)

s3 = Servos(i2c)

s4 = Servos(i2c)

s1.position(4, 60)
sleep(200)

s2.position(5, 90)
sleep(200)

s3.position(6, 60)
sleep(200)

s4.position(7, 120)
sleep(200)

def baseplate_rotate():
    global num2
    if Left_X < 100:
        num2 = num2 - 1
        s2.position(5, num2)
        sleep(5)
        if num2 <= 30:
            s2.position(5, 30)
            sleep(200)
    if Left_X > 900:
        num2 = num2 + 1
        s2.position(5, num2)
        sleep(5)
        if num2 >= 150:
            s2.position(5, 150)
            sleep(200)

def clamp_claw():
    if Right_B == True:
        s3.position(6, 180)
        sleep(10)
    if Right_B == False:
        s3.position(6, 60)
        sleep(10)

def left_arm():
    global num4
    if Left_Y > 900:
        num4 =num4 + 1
        s4.position(7, num4)
        sleep(5)
        if num4 >= 165:
            s4.position(7, 165)
            sleep(200)

    if Left_Y < 100:
        num4 = num4 - 1
        s4.position(7, num4)
        sleep(5)
        if num4 <= 35:
            s4.position(7, 35)
            sleep(200)

def right_arm():
    global num1
    if Right_Y > 800:
        num1 =num1 - 1
        s1.position(4, num1)
        sleep(5)
        if num1 <= 15:
            s1.position(4, 15)
            sleep(200)
    if Right_Y < 100:
        num1 =num1 + 1
        s1.position(4, num1)
        sleep(5)
        if num1 >= 100:
            s1.position(4, 100)
            sleep(200)
while True:
    Left_Y = pin0.read_analog()
    Left_X = pin1.read_analog()
    Right_Y = pin2.read_analog()
    Right_B = pin13.read_digital()
    print("Left_Y analog signal:",Left_Y)
    print("Left_X analog signal:",Left_X)
    print("Right_Y analog signal:",Right_Y)
    print("Right_B analog signal:",Right_B)

    baseplate_rotate()
    clamp_claw()
    left_arm()
    right_arm()
