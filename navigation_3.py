from mindstorms import MSHub, Motor, ColorSensor, App

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_right = Motor('A')
motor_left = Motor('B')
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

    previous_error = 0
    while True:
        intensity = color_sensor.get_reflected_light()
        error = target_value - intensity
        previous_error += error
        steer = error * multiplier + previous_error * 0  # find multiplier before adjusting deviate

        motor_right.start(speed + steer)
        motor_left.start(-(speed - steer))

        previous_error = error
        print(steer)


drive(15, 25, 8)
