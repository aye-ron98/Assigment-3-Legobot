from mindstorms import MSHub, MotorPair, ColorSensor, App

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')


def drive(speed, target_value, multiplier):
    """
    Drives robot.
    A function to drive the robot on the black line

    :param speed: integer between [1, 100]
    :param target_value: integer value [0, 100]
    :param multiplier: integer value, this value will control steering,
    :precondition: recommend set speed to 25
    :precondition: set target_value to edge between black tape and off course
    :precondition: recommend set multiplier to 8, lower will decrease steering higher increases
    :precondition: align robot to right edge of tape
    :postcondition: robot will follow the black line
    """

    while True:
        intensity = color_sensor.get_reflected_light()
        steer = intensity - target_value * multiplier

        motor_pair.set_default_speed(speed)
        motor_pair.start(steer)

        print(steer)


drive(15, 25, 8)
