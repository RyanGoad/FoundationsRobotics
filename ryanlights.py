import os
import sys
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import RvrStreamingServices
from sphero_sdk import SpheroRvrObserver
from sphero_sdk import Colors

rvr = SpheroRvrObserver()

def ambient_light_handler(ambient_light_data):
    print('ambient light data response: ', ambient_light_data)

def main():
    try:
        rvr.wake()

        # Give RVR time to wake up
        time.sleep(2)
        
        rvr.led_control.turn_leds_off()
        
        time.sleep(1)

        rvr.led_control.set_all_leds_rgb(red=255, green=144, blue=0)

        rvr.sensor_control.add_sensor_data_handler(
            service=RvrStreamingServices.ambient_light,
            handler=ambient_light_handler
        )

        rvr.sensor_control.start(interval=250)

        while True:
            # Delay to allow RVR to stream sensor data
            time.sleep(1)

    except KeyboardInterrupt:
        print('\nProgram terminated with keyboard interrupt.')

    finally:
        rvr.sensor_control.clear()
        rvr.close()

        # Delay to allow RVR issue command before closing
        time.sleep(.5)
        
        rvr.close()


if __name__ == '__main__':
    main()

