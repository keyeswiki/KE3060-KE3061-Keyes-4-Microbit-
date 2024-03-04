# Micro：bit 4自由度机械手臂的安装步骤

## 底座部分---安装1

安装所需零件:
![Img](./media/b5fb484289372084870b1734d95ed69f.png)

安装:
![Img](./media/429842920d73711dc6e4bf2256a8f8bd.png)
![Img](./media/b621743c4142ac102183c25e11544a32.png)
![Img](./media/e4eb066462928cc7f5af390eafd308d5.png)
![Img](./media/62b4d07dd28459db8a79fe4b0d2cd4d7.png)
![Img](./media/653805969ad3a840e15806a7c3015443.png)

完成:
![Img](./media/d5924348ed6f7311dc991e9091e7d4da.png)

## 底座舵机部分---安装2

安装所需零件:
![Img](./media/0bd2383c8706a0f9b9a975c1073a6b07.png)

安装:
![Img](./media/cd530f321519e831d9d7c67848c8ca97.png)
![Img](./media/5cb576eef19fed12c982713c5ad790f0.png)

完成:
![Img](./media/c7f70d1d538ab81f609b8d26d294c262.png)

## 左侧部分(左板+左侧舵机)---安装3

安装所需零件：
![Img](./media/b23ad1d626db04acb9f78561d7d0a156.png)

安装：
![Img](./media/946839780385dc3a417403decadb15af.png)
![Img](./media/1de33ab971f3d171820228cc15a040e5.png)

**舵机4（左侧舵机）初始化：**
安装前需要先设置舵机角度为 180°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（7），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到180°的位置。
![Img](./media/f70cf281e241a6db413b2563f374337f.png)

舵机4设置为180°的代码：
![Img](./media/805f8213328644e650171cc3ea1950b4.png)
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
![Img](./media/aa71b52567862dbc60edf50de9dd0ddb.png)

**安装摆臂：**
![Img](./media/936d39eaae36f059b1bcf2debfc85791.png)
![Img](./media/c9227ea677a14402e2a10c1b02a01a6f.png)
![Img](./media/826abd3625b579ab302a0bc7975f6ca6.png)
![Img](./media/a410a3dec6ea0869ed0b07c774ab250c.png)

完成：
![Img](./media/97eca7f44f007eb13f9a5f21bd9db1e4.png)

## 右侧部分(右板+右侧舵机)---安装4

安装所需零件：
![Img](./media/0439c5018e569ef4ae52abac7f729157.png)

安装：
<span style="color: rgb(255, 76, 65);">(注意亚克力板上的缺口方向)</span>

![Img](./media/7fb9cbfc8c7b679e5a361bb68e736318.png)
![Img](./media/1eb6423033c0467a8d56b2d26e29c1a4.png)

**舵机1（右侧舵机）初始化：**
安装前需要先设置舵机角度为 0°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（4），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到0°的位置。
![Img](./media/154f779333bf44958287a6360bf934e8.png)

舵机1设置为0°的代码：
![Img](./media/4376ac23945a7e4002c1e9617d01951d.png)
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
![Img](./media/c5679af560eb20a5e64a408b1c09f67f.png)

**安装摆臂：**
![Img](./media/b6d6dddcda1f8813a974cccffd21534e.png)
![Img](./media/506a37dc12860dcc379394cfe1d06863.png)
![Img](./media/7a320d3d98c0c88b0aa092c11aff1a44.png)
![Img](./media/8700ff9a652fff58b1016f506eba7eef.png)

完成：
![Img](./media/20795cf58cfb12fb423a068bb42f9b82.png)

## 支架部分---安装5

安装所需零件：
![Img](./media/f1f33c6375ce5ac8f925856e971939e6.png)

安装：
![Img](./media/3aec689bc1964a80e36c09d5c90e521a.png)

完成：
![Img](./media/0eb9521585cae09babe5273b9f633c37.png)

## 左侧部分+支架部分---安装6

安装所需零件：
![Img](./media/25a47bb9762d8cd65f4c72ca07b652ae.png)

安装：
![Img](./media/6d6b180970194089f00488444045ad18.png)

完成：
![Img](./media/26b1ebd2ae30dbc8afa92933614c5a77.png)

## 第6步+第4步(右侧部分)+圆柱支撑台---安装7

安装所需零件：
![Img](./media/0d646f7105bda2f3754d1b0a10ca3812.png)

安装：
<span style="color: rgb(255, 76, 65);">（注意圆柱支撑台的安装方向）</span>

![Img](./media/41587dd153d96834edc5f63adf326ec0.png)

![Img](./media/52f1609fb3ff80e5f4d18661668c729d.png)

![Img](./media/5e617fd2edb6188f322ab6b14d148a1e.png)

![Img](./media/d495deebdbc52905d1a2f61fb1daff92.png)

![Img](./media/a787c22eb78c08b0c69ffa1db2b21d76.png)

![Img](./media/e138ca44b0df641a2f61619bc2fd4b33.png)

![Img](./media/609bbabbc09132119288befb717a20f0.png)

![Img](./media/5cc58331c446113f4d665a1e69803563.png)

![Img](./media/e523e2211ab6072067298681f77b4018.png)

完成：
![Img](./media/0ed4e8eefa7311c83bfd636974b25c02.png)

## 中间部分---安装8

安装所需零件：
![Img](./media/25ea6fc5addb7ae3d641aa95535bae47.png)

安装：
![Img](./media/b87a9dea600d014267da3c310a71bc0c.png)

![Img](./media/e3116625c5bbdd570efcf471a71c337d.png)

![Img](./media/8aa9aab6ce15d8566f59b4f283b9acd9.png)

![Img](./media/7780e7414f9ecacc014851faa33ec587.png)

![Img](./media/6bab76700584a08691a5878dc47ca880.png)

![Img](./media/83b740522ebf4dc1ecfb966842334c0f.png)

![Img](./media/f52780a5528b096979bcb3cdce640ea2.png)

![Img](./media/4e474b8ea8a614145fbe290ad9c9eba9.png)

![Img](./media/c2872e28adc1c4684a512338beb0df7a.png)

![Img](./media/5b5c7f05608d98e62a65f5d7878f8283.png)

![Img](./media/16e2e051fc7dc88db617ecb4259b38d9.png)

![Img](./media/64a29af3ec448a7bb3558bdafc6520ec.png)

完成：
![Img](./media/00d3fb9ae02044ac150024ac9ea4c3f0.png)

## 爪子部分(包括舵机)---安装9

安装所需零件：
![Img](./media/e2783eaa0d44737d463067f7c9e86269.png)

安装：
![Img](./media/a0fc3dad4d6b3ba310e912f721268237.png)

![Img](./media/22f68e7ad206c8c116203cb861d0b0d6.png)

![Img](./media/e102e11bf4d665079175776c20c1e347.png)

![Img](./media/171de72a81804ebb91851dd59b93f992.png)

![Img](./media/b9f0103f61bc05b46fe29bfe2cfc5253.png)

![Img](./media/08fc887529077ac307128b7762d4d9b1.png)

![Img](./media/2101acf2f378a07db364d16e519effe8.png)

![Img](./media/3dd913e80b2957b7d31951a357ac3f90.png)

![Img](./media/1a18a580897ffaf8c4c8a05ed4d3361c.png)

![Img](./media/ca3c98f43a2646d9506903b11e03a82c.png)

![Img](./media/0f300257296221ed53474549aa6291c9.png)

**舵机3（爪子处舵机）初始化：**
安装前需要先设置舵机角度为180°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（6），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到180°的位置。
![Img](./media/50976ada0e1e3a5de659b3844459bd26.png)

舵机3设置为180°的代码：
![Img](./media/cdd2b01faae9649659c3f291f1998414.png)
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
s3.position(6, 180)
sleep(1000)
```
对应的代码在资料中也有提供，打开舵机3的初始化代码并烧录到Microbit主板中，上传完成后外接电源供电。代码如下图位置:
![Img](./media/74b8b4b68501e64ad31f7ec84fa82c1c.png)

**安装齿轮：**
![Img](./media/297aa6ee7352fa6f4963eae29af654fe.png)

完成：
![Img](./media/dac4b448c48e546a79c0096c80587023.png)

## 将上面安装好的部分相互组合---安装10

安装准备零件：
![Img](./media/457c27c289aa50279a40f83fd9e22bbe.png)

安装：
![Img](./media/feb83fa836d28a1e14f705a61939ad5b.png)

![Img](./media/f05b74108601ead5d46e81d1e1133436.png)

![Img](./media/c663301e5061f7cc3d08567ce6a94f0f.png)

![Img](./media/c4adeb0da2f9bcb91812a3ad7f53a9cc.png)

**舵机2（底座转动舵机）初始化：** 
安装前需要先设置舵机角度为90°。设置舵机角度时，将舵机连接在Microbit 16路舵机扩展板的G、V、S（5），在Microbit主控板上上传对应代码，外接电源供电后，按下Microbit主控板上的复位按键，舵机就转到90°的位置。
![Img](./media/0a40a0b1bf295bc34cd73a777cc50c1a.png)

舵机2设置为90°的代码：
![Img](./media/faaa63fc4bbd6587f2833216c29e9f0c.png)
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
![Img](./media/7a66eaf78133748acf68374ee65abf77.png)

**安装机械臂：**
![Img](./media/f3b06cb8f0134985a903dc2b6e2ca139.png)

![Img](./media/e9118053a730cb4dc8e9d09c527d9c2f.png)

完成：
![Img](./media/93993faf79bfcac9a4da3a0e4d6ef43c.png)

## 机械手臂控制部分---安装11

安装准备零件：
![Img](./media/8a6985d628142194dbb8b8f4a1f2b7c2.jpg)

安装：
![Img](./media/2ee11528de13228875f45e71eb246c27.png)

![Img](./media/5db3bf534ca1ce633ae6ce22a1a1d66a.png)

![Img](./media/ac461902564d13fe86aba330bf9e85df.png)

完成：
![Img](./media/5f92c01cd34971aa0a71c14f8962b4d7.png)

## 接线和安装microbit主板

舵机1（右侧舵机）：
![Img](./media/154f779333bf44958287a6360bf934e8.png)

![Img](./media/f7770ca434abbabc5202845510422faa.png)

![Img](./media/5295ba635edaf5051ce92de5d1932007.png)

舵机2（底座转动舵机）：
![Img](./media/0a40a0b1bf295bc34cd73a777cc50c1a.png)

![Img](./media/372ce74cd4e4cde3e2389622f13b1c2b.png)

舵机3（爪子处舵机）：
![Img](./media/50976ada0e1e3a5de659b3844459bd26.png)

![Img](./media/29565ba18c66d57ff4e13175d6505662.png)

![Img](./media/826382f8940501554504aca6cf98a9df.png)
**<span style="color: rgb(255, 76, 65);">注意：</span>由于这里舵机线不能直接连接到microbit16路舵机扩展板上的引脚，需要使用3根杜邦线将舵机线连接到microbit16路舵机扩展板上的引脚。**

舵机4（左侧舵机）：
![Img](./media/f70cf281e241a6db413b2563f374337f.png)

![Img](./media/a355151ea42462d7a89c53c679065b9e.png)

![Img](./media/9ca3a5103c1fc4431e43dc0a48d19e89.png)

插上microbit主板：
![Img](./media/c34909454062f12647a263b5eb878500.png)

左、右摇杆模块：
![Img](./media/cf00ed7f84d094260233167a55911310.png)
![Img](./media/d5188a652ad7f8df6ba73fcea2a1a0a4.png)

## 完整的Micro:bit 4自由度机械手臂
![Img](./media/320279f16edd36d3c8db5e36a0235380.png)

## 接外接电源
![Img](./media/09e66d18803074f5d732bceff3561127.jpg)

<span style="color: rgb(255, 76, 65);">用一字螺丝刀（套件提供有）将电池盒的红线端接入VIN端，将黑线端接入GND端。</span>
<br>
<br>

<span style="color: rgb(255, 76, 65);">电池盒中有弹簧的一端是负极( - )，则另一端是正极( + )。（5号电池自备）</span>






