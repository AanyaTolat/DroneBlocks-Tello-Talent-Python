from droneblocks.DroneBlocksTello import DroneBlocksTello
import time

'''
4/26:
figured out how to use the LEDs and got the library and code to work in python
next: trying to work on swarming to figure out a potential project, or work more on LEDs (possibly incorporating a data structure?)
'''
tello = DroneBlocksTello()
tello.connect()

battery_level = tello.get_battery()
print(battery_level)
tello.set_display_brightness(100)
tello.alternate_top_led(0,191,255,255,215,0,1) #flashes blue and gold
str = "b0b0rrrr0b0b0000b0b0rrrr0b0b0000rrrrrrrr00000000rrrrrrrr00000000" #american flag 🏈
tello.display_image(str)
time.sleep(3)
tello.display_character("i")
time.sleep(0.3)
tello.display_heart()
time.sleep(0.6)
tello.scroll_string("peddie", DroneBlocksTello.LEFT, DroneBlocksTello.BLUE, 2.5)
time.sleep(2.15)
tello.clear_display()
tello.display_sad(DroneBlocksTello.BLUE)
time.sleep(2)
tello.clear_display()