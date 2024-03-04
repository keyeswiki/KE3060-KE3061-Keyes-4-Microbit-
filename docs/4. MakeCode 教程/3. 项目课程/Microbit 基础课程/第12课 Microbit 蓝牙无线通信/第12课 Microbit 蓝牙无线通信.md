# 第12课 Microbit 蓝牙无线通信
![Img](./media/6806de697893af6821e037dd3e50eeef.png)

## 1.实验说明：                                                                                
Micro:bit主板了处理器内置蓝牙5.1低功耗的BLE(蓝牙 Low Energy)设备）以及2.4GHz天线，可进行蓝牙无线通信和2.4GHz无线通信。使得Micro:bit主板可以与各种蓝牙设备进行通信，包括智能手机和平板电脑。
在本实验中，主要讲解新款的Micro:bit主板实现蓝牙无线通信功能，我们可以通过连接蓝牙，实现无线传输代码（信号）功能。我们利用一个苹果系统设备（手机/iPad）和Micro:bit 主板连接，实现无线传输功能。设置安卓系统手机实现无线传输方法和苹果系统设备（手机/iPad）类似，这里就不一一介绍了。

## 2.准备：                                                                                    
（1）通过Micro USB线连接Micro:bit主板和电脑。
![Img](./media/1e429eba679d0adf7294cc4c77e08d75.png)
（2）苹果系统设备（手机/iPad）或安卓系统手机。

## 3.实验步骤：                                                                                
App下载链接：https://microbit.org/get-started/user-guide/mobile/ （安卓系统下载参考链接）

我们以苹果系统设备为例：
（1）如果你的智能手机/iPad是苹果系统的，需要先在电脑上进入网页：https://www.microbit.org/get-started/user-guide/ble-ios/ ，往下翻点击“Download pairing HEX file”下载micro:bit的固件到创建的文件夹中或电脑桌面上，并将下载好的Micro:bit固件烧入Micro:bit主板中。（<span style="color: rgb(255, 76, 65);">这一步只针对于苹果系统的智能手机/iPad，安卓系统智能手机/不需要这一步</span>）
![Img](./media/42d9c0f29061f13087b231ebd3f6843a.png)
![Img](./media/fff507d4afa87842d9e98f70c0e50ef0.png)

（2）在苹果系统设备（手机/iPad）上打开![Img](./media/904372db3737523189ff8ce4b6a89dd9.png)，在App Store的搜索框中输入“micro bit”，然后选中micro:bit 选项，会出现下载界面（如下图所示：），点击“![Img](./media/a9c7179df093d9f6eb1d39906cc2b90d.png)”，就可以下载安装对应的APP。
![Img](./media/d1ad3a8905366d883ea6a30752866924.png)

（3）苹果系统设备（手机/iPad）和Micro:bit主板配对连接。
a.APP安装成功后，打开苹果系统设备（手机/iPad）上的蓝牙。
![Img](./media/af7c7c91afadedabe9d372ab52edb380.png)

b.点击![Img](./media/e81ca01be5af70cff66813ef51b69b90.png)打开APP，先确定Micro USB数据线已经将Micro:bit主板和电脑连接上，再点击APP的第一项“**Choose micro:bit**”，开始配对蓝牙。
![Img](./media/1ba30e27f5b5cbb099ffd7d49b7b3469.png)

c.点击“**Pair a new micro:bit**”，开始配对。
![Img](./media/d08d496d5fe9a5201002df79b03cfc14.png)

d.根据提示，首先同时按住micro:bit主板上的按键A和B，然后按下micro:bit主板后面的复位&电源按钮几秒钟（按键A和B不能松开），再松开复位&电源按钮，micro:bit主板上LED点阵会显示一个密码图案。最后松开micro:bit主板上的按键A和B，接着点击“**Next**”。
![Img](./media/082aa62805725e81d73900481c1d60c5.png)
![Img](./media/25fefe3d6b631a81a6472cd979b84521.png)

e.在苹果系统手机/iPad上设置密码图案，使图案和micro:bit主板上显示的密码图案一样，点击“**Next**”。
![Img](./media/2307e6a1e3dbef0a4ac0ede8930d1749.png)

f.点击“**Next**”，出现对话框，在对话框中点击“**Pair**”。几秒钟后，配对成功，同时Micro:bit主板上的LED点阵显示“√”图案。
![Img](./media/9ac7abe5a5b1609fedd0b11e5e8d587d.png)
![Img](./media/d817c83534b2d4e4a18ca37453bc7f6e.png)
![Img](./media/6c18486e36685fad6596334410ce40af.png)
![Img](./media/0f9bf7514a01e3a8b36fc6e3b4a3f075.png)

（4）蓝牙配对成功后，开始利用APP编写代码，并上传代码。
a.点击第二项“Create Code”，进入编程界面，开始编写代码程序。
![Img](./media/335189d0e25955e8bd8859e78eee94ff.png)
![Img](./media/1c853d5586f3dece1da54c511523a111.png)
![Img](./media/5ef2d1adfc559d1546a94142094c1496.png)
![Img](./media/a85d01e948cc5e19e249f95de6e2aba6.png)

b. 将代码程序项目名称设置为“1”，点击保存图案“![Img](./media/85c9b25134a0eaacc1535f51417e1e91.png)”，保存代码程序。
![Img](./media/929759d91d5310f8f060a6983d315024.png)

c.项目代码程序保存成功后，点击第三项“**Flash**”进入上传代码程序界面。默认选择代码程序是刚刚保存的项目名称为“**1**”的代码程序，然后点击“**Flash**”上传代码程序“**1**”。
![Img](./media/f447e88d85909191e725bf167cbada24.png)
![Img](./media/b66e03a0aa90c3fc4b7ff10385560a04.png)
![Img](./media/3872186e3337b7f4cd5d07fe9961bf24.png)

d.几秒钟后，代码程序“**1**”上传成功，会显示如下图。然后micro:bit主板上的LED点阵显示跳跃的“**心**”对应图案。
![Img](./media/e5e5fc91d42ac0caee16ed4d974aa823.png)
