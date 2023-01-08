from server_config import *
from time import sleep
import requests

sleep(3)

# repeatedly trigger the lighting control logic
while True:
    try:
        requests.get(api)
    except:
        print("Error!")
    sleep(trigger_interval)
