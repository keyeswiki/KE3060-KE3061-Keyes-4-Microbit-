from microbit import sleep, i2c, button_a, button_b
from PCA9685 import *
from servo import *

# 使用默认地址(0x40)初始化PCA9685.
pwm = PCA9685.PCA9685(i2c)

# 设置适合舵机的频率为60hz.
pwm.set_pwm_freq(60)

print('Moving servo on channel 5, press Ctrl-C to quit...')

# 使用舵机2辅助类逐步移动通道5
s2 = Servos(i2c)

#设置舵机2的初始角度为30°(底座旋转舵机，通道5)
s2.position(5, 30)
sleep(200)

while True:
    if button_a.is_pressed():  # 如果microbit主板上的按键A被按下时
        for num in range(30 , 150):  # num值的范围从30到150
            num += 1        #num值每次加1
            s2.position(5, num)  #接在通道5的舵机转动num值角度
            sleep(20)
    if button_b.is_pressed():
        for num in range(30 , 150):
            num += 1
            s2.position(5, 180-num)
            sleep(20)
