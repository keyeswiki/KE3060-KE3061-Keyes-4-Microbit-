from microbit import *

Left_Y = 0    #设置变量Left_Y初始值为0
Left_X = 0
Right_Y = 0
Right_B = 0
pin14.PULL_UP     #拉高引脚14的电平
pin15.PULL_DOWN   #拉低引脚15的电平
pin14.write_digital(1)  #设置引脚14为高电平
pin15.write_digital(0)   #设置引脚15为低电平

while True:
    Left_Y = pin0.read_analog()  #将引脚P0读取的模拟值赋予变量Left_Y
    Left_X = pin1.read_analog()
    Right_Y = pin2.read_analog()
    Right_B = pin13.read_digital()
    print("Left_Y analog signal:",Left_Y)  #串口打印引脚P0读取的模拟值
    print("Left_X analog signal:",Left_X)
    print("Right_Y analog signal:",Right_Y)
    print("Right_B analog signal:",Right_B)
    sleep(200)
