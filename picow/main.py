from pir_config import *
from machine import Pin
from time import sleep
import network
import urequests as requests


# ===== various devices =====
wlan = network.WLAN(network.STA_IF)
led = Pin("LED", Pin.OUT)
pir = Pin(pir_pin, Pin.IN, Pin.PULL_DOWN)


# ===== helper functions =====
# connect to wifi
def connect_wifi():
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print("Waiting for connection...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f"Connected on {ip}")
    return ip

# disconnect wifi
def disconnect_wifi():
    wlan.disconnect()
    wlan.active(False)
    wlan.deinit()

# read motion sensor status
def get_pir():
    return pir.value()


# ===== main =====
# connect to wifi
connect_wifi()

# initialize led
led.on()
sleep(0.5)
led.off()

led_status = False

# read sensors and call API if movement is detected
while True:
    if get_pir():
        try:
            r = requests.get(api)
            r.close()
        except:
            print("Error!")
        
        if not led_status:
            led.on()
            led_status = True

        sleep(interval_on)
    else:
        if led_status:
            led.off()
            led_status = False
        
        sleep(interval_off)
