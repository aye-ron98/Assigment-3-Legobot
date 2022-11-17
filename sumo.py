from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App

import random

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')
# Initialize the Distance Sensor.
distance_sensor = DistanceSensor('D')
# Initialize the Weapon at Port E.
weapon = Motor('E')


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


def run_weapon():
    """
    Controls the weapon connected to a motor at a port.

    :postcondition: weapon connected to motor at the port is moving
    """
    count = 1
    while count < 2:
        color = color_sensor.get_color()
        if color == 'black' or color is None:
            motor_pair.stop()
            weapon.run_to_position(300, 'clockwise', 75)
            break
        else:
            weapon.run_to_position(176, 'counterclockwise', 75)
            weapon.run_to_position(300, 'clockwise', 75)
        count += 1


def fight(speed):
    """
    Robot engages in offensive sumo maneuvers.

    :param speed: an integer
    :precondition: speed must be an integer in the range [0, 100]
    :postcondition: the robot is fighting
    """
    motor_pair.set_default_speed(speed)

    while True:
        motor_pair.start(0)
        dist_cm = distance_sensor.get_distance_cm()
        color = color_sensor.get_color()
        print(color)
        if color == 'black' or color is None:
            motor_pair.stop()
            turn_randomly()
        if dist_cm is None:
            motor_pair.set_default_speed(speed)
            continue
        elif dist_cm >= 20:
            motor_pair.set_default_speed(speed * 2)
        elif dist_cm < 5:
            run_weapon()
            motor_pair.set_default_speed(speed * 5)


fight(20)
