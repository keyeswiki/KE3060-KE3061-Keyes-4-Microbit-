from microbit import sleep, i2c
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685..
pwm = PCA9685.PCA9685(i2c)

# 设置舵机频率为60hz
pwm.set_pwm_freq(60)

print('Moving servo on channel 5, press Ctrl-C to quit...')

# 舵机2使用辅助类移动通道5
s2 = Servos(i2c)

#设置舵机2初始角度(底座旋转舵机，通道5)
s2.position(5, 90)
sleep(1000)

