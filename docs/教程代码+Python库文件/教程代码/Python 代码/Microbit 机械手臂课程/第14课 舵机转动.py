from microbit import sleep, i2c
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685.
pwm = PCA9685.PCA9685(i2c)

# 设置适合舵机的频率为60hz.
pwm.set_pwm_freq(60)

print('Moving servo on channel 5, press Ctrl-C to quit...')

# 使用舵机2辅助类逐步移动通道5
s2 = Servos(i2c)
while True:
    for num in range(30 , 150):
        num += 1
        s2.position(5, num)
        sleep(20)
    for num in range(30 , 150):
        num += 1
        s2.position(5, 180-num)
        sleep(20)
