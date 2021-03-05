import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import RvrStreamingServices
from sphero_sdk import Colors

def ambient_light_handler(ambient_light_data):
    print('ambient light data response: ', ambient_light_data)

def main():
    rvr.wake()
    while false:
        getData()
        
              
def setLights(brightness):
    rvr.led_control.set_all_leds_rgb(red=brightness, green=brightness, blue=brightness)

def getData():
    rvr.sensor_control.add_sensor_data_handler(
        service=RvrStreamingServices.ambient_light,
        handler=ambient_light_handler
    )
    rvr.sensor_control.start(interval=250)
