# ryanrev2 with actual functions

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
    print('ambient light data response: ', ambient_light_data)
    brightness=ambient_light_data.get("Light")
    

def main():
    """ This program demonstrates how to set the all the LEDs of RVR using the LED control helper.
    """

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

        while True:
            # Delay to allow RVR to stream sensor data
            time.sleep(1)
        
        #pseudocode contribution
        if brightness > 255:
            brightness=255
        brightness=255-brightness
        #may need to create new variable to assign 255-brightness
        #or declare brightness as global or nonlocal e.g. global brightness \n if brightness...
        
        rvr.led_control.set_all_leds_rgb(red=brightness, green=brightness, blue=brightness)

        # Delay to show LEDs change
        time.sleep(1)
        


    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear
        
        time.sleep(.5)
        
        rvr.close()

if __name__ == '__main__':
    main()