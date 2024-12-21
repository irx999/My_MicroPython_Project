"""一个新的UI页面"""
import time

from icon import ICON_LEFT,ICON_DOWN
from machine import Pin, SoftI2C
from libs.ssd1306 import SSD1306_I2C
i2c = SoftI2C(scl=Pin(4), sda=Pin(5),freq=400000)
# 创建 OLED 对象
oled_45 = SSD1306_I2C(width=128, height=64, i2c=i2c)
# 清屏
oled_45.fill(0)



class MenuItem:
    def __init__(self, text, icon=None, callback=None ,option=None):
        self.text = text
        self.icon = icon
        self.callback = callback
        
        if option["types"] == "switch":
            self.option = option
            
        if option["state"] == True:
            self.state = True

    def select(self):
        #当被选中， 就执行callback
        if self.callback:
            self.callback()



class Menu:
    def __init__(self,oled, menuitems, selected_index=0):
         #屏幕对象
        self.oled = oled 
         #菜单集
        self.menuitems = menuitems
        #当前选中索引
        self.selected_index = selected_index
        
        self.FPS = 0

        
        
    def select(self):
        #选中当前菜单
        self.items[self.selected_index].select()
    def cartoon(self):
        #电源输入动画
        self.oled.icon(ICON_DOWN[self.FPS],24,0,)
        self.oled.icon(ICON_DOWN[self.FPS],128-24-8,0)
        
        for index, menuitem in enumerate(self.menuitems):
            #显示菜单名称
            text_x = 0
            text_x_b = 120
            text_y = 16
            text_spacing_y = 10
            if index < 4:
                if menuitem.state:
                    self.oled.icon(ICON_LEFT[self.FPS],
                                   text_x,
                                   text_y+(index)*text_spacing_y,1)
            else:
                if menuitem.state:
                    self.oled.icon_r(ICON_LEFT[self.FPS],
                                   text_x_b,
                                   text_y+(index-4)*text_spacing_y,1)
        
        

        self.oled.show()
        self.FPS +=1
        if self.FPS == 8:
            self.FPS = 0
        self.ui_basics()
    def ui_basics(self):
        # 一个UI 基础的页面
        #分割线
        for x in range(16,128-16):
            self.oled.pixel(x,12,1)
            self.oled.pixel(x,56,1)
        for y in range(12,56):
            self.oled.pixel(16,y,1)
            self.oled.pixel(128-16,y,1)
        self.oled.text("POWER IN",
                       (128 - len("POWER IN") * 8)//2,
                       0)
        
        for index, menuitem in enumerate(self.menuitems):
            #显示菜单名称
            text_x = 18
            text_x_b = 68
            text_y = 16
            text_spacing_y = 10
            if index < 4:
                self.oled.text(menuitem.text,
                               text_x,
                               text_y+(index)*text_spacing_y,1)
            else:
                self.oled.text(menuitem.text,
                               text_x_b,
                               text_y+(index-4)*text_spacing_y,1)
            
        self.oled.show()
    
if __name__ == '__main__':
    #实例化一个菜单
    switch = {'types':"switch",'state':True}
    menuitems = [
        MenuItem("<-12V", option = switch),
        MenuItem("<-12V", option = switch),
        MenuItem("<-12V", option = switch),
        MenuItem("<-PWM", option = switch),
        MenuItem("12V->", option = switch),
        MenuItem("12V->", option = switch),
        MenuItem("12V->", option = switch),
        MenuItem("PWM->", option = switch),
    ]
    menu = Menu(oled_45,menuitems)
    
    
    
    while True:
        menu.cartoon()
    
    