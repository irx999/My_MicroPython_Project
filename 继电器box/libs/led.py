'''esp32 自带的led 灯珠控制，'''

from time import sleep
import  neopixel
from machine import Pin
#创建灯珠实例"
n = 1
p = 48 #esp32 s3 的灯珠是48号
np = neopixel.NeoPixel(Pin(10, Pin.OUT), n)


red = (25,0,0)
green = (0,25,0)
blue = (0,0,25)
white = (25,25,25)
black = (0,0,0)


def np_sparkle(colors:list,number_of_flashes=2,step=0.5):
    '''闪烁灯珠'''
    for i in range(number_of_flashes):
        for color in colors:
            np[0]=color
            np.write()
            sleep(step)
    np[0]=black
    np.write()

def  gradient(colors,duration = 1 ):
    '''渐变'''
    for index in range(len(colors)-1):
        r1,g1,b1 = colors[index]
        r2,g2,b2 = colors[index+1]
        step = max((r2-r1),(g2-g1),(b2-b1))
        print(step)
        r_step = (r2-r1)/step
        g_step = (g2-g1)/step
        b_step = (b2-b1)/step
        for i in range(step):
            r = abs(int(r1 + r_step*i))
            g = abs(int(g1 + g_step*i))    
            b = abs(int(b1 + b_step*i))
            np[0]=(r,g,b)
            np.write()
            sleep(duration/step)
            #sleep(1/25)
    np[0]=black
    np.write()
def error(n = 3):

    '''错误'''
    for i in range(n):
        np[0]=(255,0,0)
        np.write()
        sleep(0.5)
        np[0]=(0,0,0)
        np.write()
        sleep(0.5)


if __name__ == '__main__':

    np_sparkle([red,green,blue],number_of_flashes=2,step=0.5)
    #gradient([red,blue,green],1)
    error()
