from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math


# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')


def course_correction(light_offset, correction_value, multiplier):
    """
    Calculate course correction scalar.
    Function to examine the difference between centerline black and current position. Will return an integer to be used
    to scale motor speed.
    :param light_offset: an integer [0, 100]
    :precondition: light_offset must be an integer [1, 100]
    :postcondition: will calculate the difference between 65 and light_offset
    :return: the difference between 65 and light_offset as an integer
    >>> course_correction(90)
    -12
    >>> course_correction(65)
    0
    >>> course_correction(40)
    12
    >>> course_correction(0)
    32
    >>> course_correction(100)
    -17
    """
    proportional_error = light_offset - correction_value
    return multiplier * proportional_error


def drive(speed, correction_value, multiplier):
    """
    Drives robot.
    A function to drive the robot on the black line
    :param speed: integer between [1, 100]
    :precondition: speed must be an integer between [1, 100]
    :postconidion: wheel motors will move at rotation rate equivalent to speed
    """
    motor_pair.set_default_speed(speed)

    while True:
        intensity = color_sensor.get_reflected_light()
        correction = course_correction(intensity, correction_value, multiplier)
        motor_pair.start(correction)


drive(5, 25, 5)
