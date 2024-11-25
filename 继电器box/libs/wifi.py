""" wifi链接 """
import network
import time

def connect_wifi():
    """ 链接wifi """
    ssid = 'CQTN 2.4G'
    password = 'cqld61601360'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() is False:
        print('Waiting for connection...')
        time.sleep(1)
    print('Connected on {ip}'.format(ip=wlan.ifconfig()[0]))


if __name__ == '__main__':
    connect_wifi()
