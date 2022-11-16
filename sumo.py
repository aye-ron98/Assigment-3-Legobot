from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
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

    :postcondition: the robot is facing a direction that is a random angle from its original direction
    """
    hub.motion_sensor.reset_yaw_angle()
    current_angle = hub.motion_sensor.get_yaw_angle()
    random_angle = random.randint(150, 180)
    while current_angle < random_angle:
        current_angle = hub.motion_sensor.get_yaw_angle()
        motor_pair.start(100)
    motor_pair.stop()


def fight(speed, tape_intensity):
    """
    Robot engages in offensive sumo maneuvers.

    :param speed: an integer
    :param tape_intensity: an integer
    :precondition: speed must be an integer
    :precondition: tape_intensity must be an integer
    :postcondition: the robot is fighting
    """
    motor_pair.set_default_speed(speed)

    while True:
        motor_pair.start(0)
        dist_cm = distance_sensor.get_distance_cm()
        if color_sensor.get_reflected_light() <= tape_intensity:
            motor_pair.stop()
            turn_randomly()
        if dist_cm is None:
            continue
        elif dist_cm >= 15:
            motor_pair.set_default_speed(speed * 2)
        elif dist_cm < 15:
            motor_pair.set_default_speed(speed * 3)


fight(20, 19)
