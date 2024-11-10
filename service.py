from flask import Flask, request

from gpiozero import OutputDevice
pump = OutputDevice(pin=4, active_high=True, initial_value=False)

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'WaterPi'

@app.route('/pump', methods=['GET'])
def get_pump_status():
    status = 'ON' if pump.value else 'OFF'
    return status

@app.route('/pump', methods=['PUT'])
def set_pump_status():
    print("SOMEONE TRIES TO SET PUMP STATUS")
    content = request.json
    print(content)
    if(content["status"] == "ON"):
      print("turn on the pump")
      pump.on()
      return "Pump is now ON"
    elif (content["status"] == "OFF"):
      print("turn off the pump")
      pump.off()
      return "Pump is now OFF"
    else:
      print("don't know what to do")
      return "ERROR: Impossible to determine destination status"
