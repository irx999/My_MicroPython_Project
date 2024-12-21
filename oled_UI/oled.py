""" oled_UI. """
from machine import Pin, SoftI2C
import time

from libs.ssd1306 import SSD1306_I2C
i2c = SoftI2C(scl=Pin(4), sda=Pin(5),freq=400000)
# 创建 OLED 对象
oled = SSD1306_I2C(width=128, height=64, i2c=i2c)

# 清屏
oled.fill(0)

# 定义图标数据
CHECK_ICON = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

WARNING_ICON_32 = [
    [0, 0, 0, 1, 1, 0, 0, 0] * 3,
    [0, 0, 1, 1, 1, 1, 0, 0] * 3,
    [0, 1, 1, 1, 1, 1, 1, 0] * 3,
    [1, 1, 1, 1, 1, 1, 1, 1] * 3,
    [1, 1, 1, 1, 1, 1, 1, 1] * 3,
    [0, 1, 1, 1, 1, 1, 1, 0] * 3,
    [0, 0, 1, 1, 1, 1, 0, 0] * 3,
    [0, 0, 0, 1, 1, 0, 0, 0] * 3
] * 4
# 菜单项类
class MenuItem:
    def __init__(self, text, icon=None, callback=None):
        self.text = text
        self.icon = icon
        self.callback = callback

    def select(self):
        if self.callback:
            self.callback()

# 菜单类
class Menu:
    def __init__(self, items, selected_index=0):
        self.items = items
        self.selected_index = selected_index

    def up(self):
        self.selected_index = (self.selected_index - 1) % len(self.items)
        oled.text("<", 1, 55)
        oled.show()
        self.toggle_animation_text()

    def down(self):
        self.selected_index = (self.selected_index + 1) % len(self.items)
        oled.text(">", 120, 55)
        oled.show()
        self.toggle_animation_text()

    def toggle_animation_text(self):
        """ 文字部分的动画 """
        text_x = (128 - len(self.items[self.selected_index].text) * 8) // 2
        for i in range(0,68-50,5):
            #oled.fill(0)
            oled.show()
            #time.sleep(0.01)
            oled.fill_rect(30, 55, 80, 30, 0)
            oled.text(self.items[self.selected_index].text, text_x,68-i, )
            self.toggle_animation_icon(self.items[self.selected_index])
            # 分割线和其他组成
            oled.text('-'*90,1, 40)
            oled.text("<-", 8, 55)
            oled.text("->", 128-8*3, 55)
            oled.show()
    def toggle_animation_icon(self,item):
        """ 图标部分的动画 """
        icon_width = 24  # 原始图标宽度
        icon_height = 24  # 原始图标高度
        icon_x = (128 - icon_width) // 2  # 图标水平居中
        icon_y = 10  # 图标从第10行开始


        for y in range(icon_height):
            for x in range(icon_width):
                if item.icon[y][x] == 1:
                    oled.pixel(x + icon_x, y + icon_y, 1)


    def select(self):
        self.items[self.selected_index].select()

    def display(self):
        oled.fill(0)

        icon_width = 24  # 原始图标宽度
        icon_height = 24  # 原始图标高度
        icon_x = (128 - icon_width) // 2  # 图标水平居中
        icon_y = 10  # 图标从第10行开始
        text_y = 55  # 文本从第40行开始

        for index, item in enumerate(self.items):
            # 图标
            self.toggle_animation_icon(item)
            # 分割线
            oled.text('-'*90,1, 40)
            # 计算文本位置
            text_x = (128 - len(item.text) * 8) // 2  # 文本水平居中
            if index == self.selected_index:
                # 选中状态
                oled.text(item.text, text_x, text_y, 2)


            oled.text("<-", 8, text_y)
            oled.text("->", 128-8*3, text_y)

        oled.show()

# 示例菜单项
def on_option_select():
    print("Option selected")

items = [
    MenuItem("Setting", WARNING_ICON_32,),
    MenuItem("Menus1", WARNING_ICON_32, on_option_select),
    MenuItem("BUG-TEST", WARNING_ICON_32)
]

menu = Menu(items)

# 主循环
while True:
    menu.display()

    uesr = input()
    if uesr == 'w':
        menu.up()
    elif uesr == 'a':
        menu.select()
    elif uesr == 's':
        menu.down()




if __name__ == '__main__':
    oled.text('Hello, XX!', 1, 1)
    oled.text('-'*90, 1, 10)
    oled.show()

