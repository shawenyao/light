from server_config import *
from flask import *
from time import time
from waitress import serve
import os


# ===== the flask server =====
# instantiate this node
app = Flask(__name__)

# if movement is detected
@app.route("/picow/pir", methods=["GET"])
def movement_detected():
    last_movement = light.movement_detected()
    response = {"status": "success", "last_movement": last_movement}
    return jsonify(response), 200

# trigger to evaluate whether to turn on or off the light
@app.route("/light/control", methods=["GET"])
def control_light():
    light.control_light()
    response = {"status": "success"}
    return jsonify(response), 200

# the Light object to model and control its state
class Light(object):
    def __init__(self):
        # the last time when movement is detected
        self.last_movement_time = 0
        # set initial status of the light
        self.kasa_api(status=False)

    def movement_detected(self):
        # store the timestamp of the last time when movement is detected
        self.last_movement_time = time()
        return self.last_movement_time
    
    def control_light(self):
        if (not self.status) and (time() - self.last_movement_time < duration):
            self.kasa_api(status=True)
        elif (self.status) and (time() - self.last_movement_time >= duration):
            self.kasa_api(status=False)

    def kasa_api(self, status):
        self.status = status
        if self.status:
            os.system(f"kasa --host {kasa_host} --type plug on")
        else:
            os.system(f"kasa --host {kasa_host} --type plug off")


# ===== main ====
if __name__ == "__main__":
    # instantiate the light
    light = Light()
    
    # start serving the app
    serve(app, host="0.0.0.0", port=server_port)
