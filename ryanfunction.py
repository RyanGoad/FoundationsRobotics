import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors
#sensor streaming
from sphero_sdk import RvrStreamingServices

brightness=0

rvr = SpheroRvrObserver()

#sensor streaming
def ambient_light_handler(ambient_light_data):
    global brightness
    brightness=ambient_light_data.get('AmbientLight').get('Light', 0)
    print(brightness)
    if brightness > 255:
        brightness=255
    brightness=255-brightness

    
    
def main():
    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)
        
        #sensor streaming        
        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )

        rvr.sensor_control.start(interval=250)
        
        #pseudocode contribution
        global brightness
        print('brightness at logic: ', brightness)
        rvr.led_control.set_all_leds_rgb(red=brightness, green=brightness, blue=brightness)

        while True:
            time.sleep(1)
        # Delay to show LEDs change
        #time.sleep(1)
        
    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear
        
        time.sleep(.5)
        
        rvr.close()

if __name__ == '__main__':
    main()
