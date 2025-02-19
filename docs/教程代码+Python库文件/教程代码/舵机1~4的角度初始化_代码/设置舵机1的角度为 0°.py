from microbit import sleep, i2c
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685.
pwm = PCA9685.PCA9685(i2c)

# 设置舵机频率为60hz
pwm.set_pwm_freq(60)

print('Moving servo on channel 4, press Ctrl-C to quit...')

# 舵机1使用辅助类移动通道4
s1 = Servos(i2c)

# 设置舵机1初始角度(右舵机，通道4)
s1.position(4, 0)
sleep(1000)

