""" wifi链接 """
import network
import time

def connect():
    """ 链接wifi """
    ssid = 'cold24'
    password = '123456789'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() is False:
        print('Waiting for connection...')
        time.sleep(1)
    print('Connected on {ip}'.format(ip=wlan.ifconfig()[0]))


if __name__ == '__main__':
    connect()
