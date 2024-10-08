# Micro：bit 4自由度机械手臂的安装步骤

## 底座部分---安装1

### 安装所需零件:
![Img](/media/img-20230324195717.png)

### 安装:
![Img](/media/img-20230324195727.png)
![Img](/media/img-20230324195739.png)
![Img](/media/img-20230324195743.png)
![Img](/media/img-20230324195747.png)
![Img](/media/img-20230324195752.png)

### 完成:
![Img](/media/img-20230324195806.png)

## 底座舵机部分---安装2

### 安装所需零件:
![Img](/media/img-20230324195840.png)

### 安装:
![Img](/media/img-20230324195852.png)
![Img](/media/img-20230324195856.png)

### 完成:
![Img](/media/img-20230324195908.png)

## 左侧部分(左板+左侧舵机)---安装3

### 安装所需零件：
![Img](/media/img-20230404094912.png)

### 安装：
![Img](/media/img-20230404094924.png)
![Img](/media/img-20230404094940.png)

**舵机4（左侧舵机）初始化：** **<span style="color: rgb(2, 30, 170);"><span style="color: rgb(255, 41, 65);">（注意：舵机安装前必须进行初始化，否则安装后导入代码很容易导致舵机卡死）</span></span>**
安装前需要先设置舵机角度为 180°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（7），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到180°的位置。
![Img](/media/img-20230404095029.png)

舵机4设置为180°的代码：
![Img](/media/img-20230404114254.png)
```
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

```
对应的代码在资料中也有提供，打开舵机8的初始化代码并烧录到Microbit主板中，上传完成后外接电源供电。代码如下图位置:
![Img](/media/img-20230404114417.png)

**安装摆臂：**
![Img](/media/img-20230404095133.png)
![Img](/media/img-20230404095140.png)
![Img](/media/img-20230404095144.png)
![Img](/media/img-20230404095150.png)

### 完成：
![Img](/media/img-20230404095202.png)

## 右侧部分(右板+右侧舵机)---安装4

### 安装所需零件：
![Img](/media/img-20230404095440.png)

### 安装：
<span style="color: rgb(255, 76, 65);">(注意亚克力板上的缺口方向)</span>

![Img](/media/img-20230404095457.png)
![Img](/media/img-20230404095520.png)

**舵机1（右侧舵机）初始化：** **<span style="color: rgb(2, 30, 170);"><span style="color: rgb(255, 41, 65);">（注意：舵机安装前必须进行初始化，否则安装后导入代码很容易导致舵机卡死）</span></span>**
安装前需要先设置舵机角度为 0°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（4），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到0°的位置。
![Img](/media/img-20230404095624.png)

舵机1设置为0°的代码：
![Img](/media/img-20230404114529.png)
```
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
```
对应的代码在资料中也有提供，打开舵机1的初始化代码并烧录到Microbit主板中，上传完成后外接电源供电。代码如下图位置:
![Img](/media/img-20230404114627.png)

**安装摆臂：**
![Img](/media/img-20230404095714.png)
![Img](/media/img-20230404095718.png)
![Img](/media/img-20230404095722.png)
![Img](/media/img-20230404095727.png)

### 完成：
![Img](/media/img-20230404095749.png)

## 支架部分---安装5

### 安装所需零件：
![Img](/media/img-20230404095815.png)

### 安装：
![Img](/media/img-20230404095828.png)

### 完成：
![Img](/media/img-20230404095848.png)

## 左侧部分+支架部分---安装6

### 安装所需零件：
![Img](/media/img-20230404095916.png)

### 安装：
![Img](/media/img-20230404095931.png)

### 完成：
![Img](/media/img-20230404095947.png)

## 第6步+第4步(右侧部分)+圆柱支撑台---安装7

### 安装所需零件：
![Img](/media/img-20230404100013.png)

### 安装：
<span style="color: rgb(255, 76, 65);">（注意圆柱支撑台的安装方向）</span>

![Img](/media/img-20230404100028.png)

![Img](/media/img-20230404100049.png)

![Img](/media/img-20230404100054.png)

![Img](/media/img-20230404100057.png)

![Img](/media/img-20230404100103.png)

![Img](/media/img-20230404100107.png)

![Img](/media/img-20230404100111.png)

![Img](/media/img-20230404100115.png)

![Img](/media/img-20230404100119.png)

### 完成：
![Img](/media/img-20230404100134.png)

## 中间部分---安装8

### 安装所需零件：
![Img](/media/12345.png)

### 安装：
![Img](/media/img-20230404100457.png)

![Img](/media/img-20230404100502.png)

![Img](/media/img-20230404100508.png)

![Img](/media/img-20230404100512.png)

![Img](/media/img-20230404100517.png)

![Img](/media/img-20230404100521.png)

![Img](/media/img-20230404100526.png)

![Img](/media/img-20230404100530.png)

![Img](/media/123456.png)

![Img](/media/12345678.png)

![Img](/media/img-20230404100547.png)

![Img](/media/img-20230404100551.png)

### 完成：
![Img](/media/img-20230404100607.png)

## 爪子部分(包括舵机)---安装9

### 安装所需零件：
![Img](/media/img-20230407083727.png)

### 安装：
![Img](/media/img-20230404100949.png)

![Img](/media/img-20230404100954.png)

![Img](/media/img-20230404100958.png)

![Img](/media/img-20230404101002.png)

![Img](/media/img-20230404101008.png)

![Img](/media/img-20230404101013.png)

![Img](/media/img-20230404101017.png)

![Img](/media/img-20230404101022.png)

![Img](/media/img-20230407083815.png)

![Img](/media/img-20230407083823.png)

![Img](/media/img-20230404101059.png)

**舵机3（爪子处舵机）初始化：** **<span style="color: rgb(2, 30, 170);"><span style="color: rgb(255, 41, 65);">（注意：舵机安装前必须进行初始化，否则安装后导入代码很容易导致舵机卡死）</span></span>**
安装前需要先设置舵机角度为60°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（6），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到60°的位置。
![Img](/media/img-20230404101152.png)

舵机3设置为60°的代码：
![Img](/media/img-20230404114701.png)

```
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
```
对应的代码在资料中也有提供，打开舵机3的初始化代码并烧录到Microbit主板中，上传完成后外接电源供电。代码如下图位置:
![Img](/media/img-20230404114758.png)

**安装齿轮：**
![Img](/media/img-20230404101325.png)

### 完成：
![Img](/media/img-20230404101341.png)

## 将上面安装好的部分相互组合---安装10

### 安装准备零件：
![Img](/media/img-20230404101410.png)

### 安装：
![Img](/media/img-20230404101424.png)

![Img](/media/img-20230404101429.png)

![Img](/media/img-20230404101435.png)

![Img](/media/img-20230404101439.png)

**舵机2（底座转动舵机）初始化：**  **<span style="color: rgb(2, 30, 170);"><span style="color: rgb(255, 41, 65);">（注意：舵机安装前必须进行初始化，否则安装后导入代码很容易导致舵机卡死）</span></span>**
安装前需要先设置舵机角度为90°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（5），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到90°的位置。
![Img](/media/img-20230404101458.png)

舵机2设置为90°的代码：
![Img](/media/img-20230404114826.png)
```
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
```
对应的代码在资料中也有提供，打开舵机2的初始化代码并烧录到Microbit主板中，上传完成后外接电源供电。代码如下图位置:
![Img](/media/img-20230404115006.png)

**安装机械臂：**
![Img](/media/img-20230404101539.png)

![Img](/media/img-20230404101543.png)

### 完成：
![Img](/media/img-20230404101606.png)

## 机械手臂控制部分---安装11

### 安装准备零件：
![Img](/media/img-20230407090938.jpg)

### 安装：
![Img](/media/img-20230406114422.png)

![Img](/media/img-20230406114506.png)

![Img](/media/img-20230406114524.png)

### 完成：
![Img](/media/img-20230406114541.png)

## 接线和安装microbit主板

### 舵机1（右侧舵机）：
![Img](/media/img-20230404101813.png)

![Img](/media/img-20230404101818.png)

![Img](/media/img-20230404101828.png)

### 舵机2（底座转动舵机）：
![Img](/media/img-20230404101846.png)

![Img](/media/img-20230404101850.png)

### 舵机3（爪子处舵机）：
![Img](/media/img-20230404101914.png)

![Img](/media/img-20230404101919.png)

![Img](/media/img-20230404101925.png)
**<span style="color: rgb(255, 76, 65);">注意：</span>由于这里舵机线不能直接连接到microbit16路舵机扩展板上的引脚，需要使用3根杜邦线将舵机线连接到microbit16路舵机扩展板上的引脚。**

### 舵机4（左侧舵机）：
![Img](/media/img-20230404101941.png)

![Img](/media/img-20230404101945.png)

![Img](/media/img-20230404101949.png)

### 插上microbit主板：
![Img](/media/img-20230404102006.png)

### 左、右摇杆模块：
![Img](/media/img-20230404112910.png)
![Img](/media/img-20230407090206.png)

## 完整的Micro:bit 4自由度机械手臂
![Img](/media/img-20230407090047.png)

## 接外接电源
![Img](/media/img-20230510173307.jpg)

<span style="color: rgb(255, 76, 65);">用一字螺丝刀（套件提供有）将电池盒的红线端接入VIN端，将黑线端接入GND端。</span>
<br>
<br>

<span style="color: rgb(255, 76, 65);">电池盒中有弹簧的一端是负极( - )，则另一端是正极( + )。（5号电池自备）</span>





