# 这里是存放继电器模块的
from machine import Pin
import time
from oled import *

setting = {
    "FAN_1" : Pin(15, Pin.OUT),
    "LED_1" : Pin(16, Pin.OUT),
    "LED_2" : Pin(17, Pin.OUT),
    "LED_3" : Pin(18, Pin.OUT),
}
def test():

    up_oled(setting)
    time.sleep(1)
    setting["FAN_1"].value(1)
    up_oled(setting)

    time.sleep(1)
    setting["FAN_1"].value(0)
    up_oled(setting)
    
pin_button1 = Pin(7, Pin.IN, Pin.PULL_DOWN)
pin_button2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
    
    
def test2():
    vcc1 = Pin(6, Pin.OUT)
    vcc2 = Pin(10,Pin.OUT)
    vcc1.value(1)
    vcc2.value(1)
    
    #菜单
    menus = ['FAN_1', 'LED_1', 'LED_2', 'LED_3']
    
    
    index = 0
    up_oled(index,setting)
    try:
        while True:
            if pin_button1.value() == 1:
                # 切换当前选中设置项的状态
                v = 1 if setting[menus[index]].value() == 0 else 0
                setting[menus[index]].value(v)
                up_oled(index, setting)
                time.sleep(0.2)
                
                # 如果是直接关闭风扇 就关闭所有的灯
                if index == 0 and v ==  0:
                    for i in range(1, 4):
                        setting[menus[i]].value(0)  # 关闭每个灯
                    up_oled(index, setting)
                    time.sleep(0.2)

                # 检查是否有灯开启，如果有，则确保风扇开启
                lights_on = any(setting[menus[i]].value() for i in range(1, 4))
                if lights_on:
                    setting[menus[0]].value(1)  # 开启风扇
                    up_oled(index, setting)
                    time.sleep(0.2)
                
                    
            
            #光标切换
            if pin_button2.value() == 1:
                index += 1
                if index == 4:
                    index = 0
                up_oled(index,setting)
                time.sleep(0.2)
    except:
        print("end")
    finally:
        oled_close()
    
if __name__ == '__main__':
    test2()

