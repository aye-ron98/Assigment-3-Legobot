from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import random


# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')
# Initialize the Distance Sensor.
distance_sensor = DistanceSensor('D')


def turn_randomly():
    """
    Turns the robot in a random angle selected from the range of integers [110,180]

    """
    hub.motion_sensor.reset_yaw_angle()
    random_angle = random.randint(110,180)
    while hub.motion_sensor.get_yaw_angle() < random_angle:
        motor_pair.start(100)
    motor_pair.stop()


def fight():
    """
    Robot engages in offensive sumo maneuvers.

    """
    motor_pair.set_default_speed(10)

    while True:
        motor_pair.start(0)
        dist_cm = distance_sensor.get_distance_cm()
        print(dist_cm)
        if color_sensor.get_color() == 'black':
            turn_randomly()
        if dist_cm is None:
            continue
        if dist_cm >= 15:
            motor_pair.set_default_speed(20)
        elif dist_cm < 14:
            motor_pair.set_default_speed(30)


fight()
