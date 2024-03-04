from microbit import sleep, i2c
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685.
pwm = PCA9685.PCA9685(i2c)

# 设置舵机频率为60hz
pwm.set_pwm_freq(60)

print('Moving servo on channel 7, press Ctrl-C to quit...')

# 舵机4使用辅助类移动通道7
s4 = Servos(i2c)

# 设置舵机4初始角度(左舵机，通道7)
s4.position(7, 180)
sleep(1000)

