from droneblocks.DroneBlocksTello import DroneBlocksTello
import time


def main(dronblocks_tello):
    battery_level = dronblocks_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Alternate Top LED between red and blue (raw command)")
    rtn = dronblocks_tello.send_command_with_return("EXT led bl 1.0 255 0 0 0 0 255")
    print(rtn)
    time.sleep(3)

    print("Alternate Top LED at a freq of 1.0")
    rtn = dronblocks_tello.alternate_top_led(r1=0, g1=255, b1=0, r2=255, g2=0, b2=255, freq=1.0)
    print(rtn)
    time.sleep(3)

    for x in range(1, 30, 5):
        freq = x / 10
        print(f"Alternate between Red and Blue at frequency: {freq}")
        dronblocks_tello.alternate_top_led(r1=255, g1=0, b1=0, r2=0, g2=0, b2=255, freq=freq)
        time.sleep(5)

    print("Set LED to OFF")
    rtn = dronblocks_tello.set_top_led(r=0, b=0, g=0)
    print(rtn)


if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()
    try:
        print("Connect to Tello Drone")
        db_tello.connect()

        print("Turn motor to stay cool")
        db_tello.turn_motor_on()

        main(db_tello)

    finally:
        db_tello.turn_motor_off()