# A Distributed Motion-Controlled Lighting System

https://www.shawenyao.com/A-Distributed-Motion-Controlled-Lighting-System/

## Overview
* `picow` code to be run on a Raspberry Pi Pico W
* `server` code to be run on a Raspberry Pi 4

## Instructions on deployment
1. `cd ~`
2. `git clone https://github.com/shawenyao/light.git`
3. Edit `~/light/server/server_config.py` and `~/light/picow/pir_config.py` as necessary
4. Upload all files in `picow` to a Raspberry Pi Pico W
5. `~/light/server/start` to start the server
6. `~/light/server/stop` to stop the server
