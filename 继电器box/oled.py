from machine import Pin, SoftI2C

from time import sleep
from libs.ssd1306 import SSD1306_I2C
i2c = SoftI2C(scl=Pin(4), sda=Pin(5),freq=400000)
# 创建 OLED 对象
oled = SSD1306_I2C(width=128, height=64, i2c=i2c)

# 清屏
oled.fill(0)



menus = ['FAN_1', 'LED_1', 'LED_2', 'LED_3']


def wifi_info(wifi_wlan):
    oled.text('Hello, !', 1, 1)
    oled.text('My IP is ', 1, 10)
    oled.text(wifi_wlan[0],1,20)
    oled.show()
    

def up_oled(index,setting):
    #index = index
    #time = 0
    oled.fill(0)
    oled.text('Hello, XX!', 1, 1)
    oled.text('-'*90, 1, 10)
    
    for i  in [0,1,2,3]:
        oled.text((">"if index == i else " ") + menus[i] + "-->" + ("Open" if setting[menus[i]].value() ==1  else "Close")
                  ,10,i*10+20)
    oled.show()
def oled_close():
    oled.fill(0)
    oled.show()
    
        
if __name__ == '__main__':
    # from electric  import setting 
    # up_oled(setting)                                                 

    oled.text('Hello, XX!', 1, 1)
    oled.text('-'*90, 1, 10)
    oled.show()