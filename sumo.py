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
    Turns the robot clockwise in a random angle selected from the range of integers [150,180].

    :precondition: hub motion sensor is functional
    :precondition: a pair of motors to drive wheels are connected to hub
    :postcondition: the robot is facing a direction that is a clockwise random angle in the range [150,180]
                    from its original direction
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
    Swings the weapon connected to the motor at a port if not standing on black boundary.

    :precondition: a motor with weapon attached is connected to hub
    :postcondition: if not on black line then weapon connected to motor swings
    :postcondition: if on black line then stop the robot and reset weapon position
    """
    color = color_sensor.get_color()
    if color == 'black' or color is None:
        motor_pair.stop()
        weapon.run_to_position(300, 'clockwise', 75)
    else:
        weapon.run_to_position(176, 'counterclockwise', 75)
        weapon.run_to_position(300, 'clockwise', 75)


def fight(speed):
    """
    Robot engages in offensive sumo maneuvers.

    :param speed: an integer
    :precondition: speed must be an integer in the range [1, 100]
    :precondition: a distance sensor is connected to hub
    :precondition: a pair of motors to drive wheels are connected to hub
    :postcondition: the robot is moving forward and fighting and staying within black boundaries by turning
    """
    motor_pair.set_default_speed(speed)

    while True:
        motor_pair.start(0)
        dist_cm = distance_sensor.get_distance_cm()
        color = color_sensor.get_color()
        if color == 'black' or color is None:
            motor_pair.stop()
            turn_randomly()
        if dist_cm is None:
            motor_pair.set_default_speed(speed)
        elif dist_cm >= 20:
            motor_pair.set_default_speed(speed * 2)
        elif dist_cm < 5:
            run_weapon()
            motor_pair.set_default_speed(speed * 5)


fight(20)
