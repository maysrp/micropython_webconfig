# micropython_webconfig

## 安装
使用micropython下的异步web框架（nanoweb）在ESP8266 上使用web界面修改配置
 [NanoWeb](https://github.com/hugokernel/micropython-nanoweb)
 下载[nanoweb.py ](https://github.com/hugokernel/micropython-nanoweb)
 上传nanoweb.py 和web.py  
 
 如果esp8266上没有uasyncio库请先下载uasyncio（mpy1.14版本以下请不要使用该项目）(esp8266 esp01s没有该库)
 
 ### 按照uasyncio
首先将你的设备联网 步骤略

 ```
 import upip
 upip.install("micropython-uasyncio")
 ```
 ## 使用
 ### micropython设备
 ```
 import web
 web.ha=["wifi","password","name"]
 web.loop.run_forever()
 
 ```
 即可使用该设置
 ### 你的手机或者平板 PC
 WiFi连接mpy热点，密码为空。
浏览器打开192.168.4.1 即可进入配置界面，配置的值更具你设置的ha的值而定，修改配置后文件保存在 config.ini 中，请读取文件。

## 建议
可以搭配GPIO或者判断联网状态进行触发该web界面，修改配置后重启电源等来达到通过web配置的目的。

