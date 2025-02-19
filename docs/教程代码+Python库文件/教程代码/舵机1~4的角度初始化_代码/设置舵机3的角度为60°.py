from microbit import sleep, i2c
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685.
pwm = PCA9685.PCA9685(i2c)

# 设置舵机频率为60hz.
pwm.set_pwm_freq(60)

print('Moving servo on channel 6, press Ctrl-C to quit...')

# 舵机3使用辅助类移动通道6
s3 = Servos(i2c)

# 设置舵机3初始角度(爪子处舵机，通道6)
s3.position(6, 60)
sleep(1000)

