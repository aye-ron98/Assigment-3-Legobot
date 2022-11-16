from mindstorms import MSHub, MotorPair, ColorSensor, App

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')


def scale(light, tape, floor, steer_max, steer_range, light_range):
    """
    Normalize scale factor between desired maximum and minimum turning values.
    ***This should ensure robot does not have preference to right turns***

    :param light: amount from light sensor
    :param tape: amount of reflection from middle of tape
    :param floor: amount of reflected light from floor (out of bound)
    :param steer_max: max turn amount (bind robot to these turns)
    :return: scale factor to correct steering
    """
    return int(-95 + (((light - tape) * steer_range)) / light_range)


def drive(tape, floor, steer_max):
    """
    Drives robot.
    A function to drive the robot on the black line

    :param target_value: reflection between tape and black line
    :param tape: reflection from middle of line (lower bound)
    :param floor: reflection from floor (upper bound)
    :postcondition: robot will follow the black line
    """
    steer_range = steer_max - (-95)
    light_range = floor - tape

    while True:
        intensity = color_sensor.get_reflected_light()
        steer = scale(intensity, tape, floor, steer_max, steer_range, light_range)
        if intensity <= (tape - 1):
            motor_pair.start_at_power(-35, (-1 * int(steer * 1.5)))

        else:
            motor_pair.start_at_power(40, steer)

        print('light sensor: {0}, turn value {1}'.format(intensity, steer))


drive(21, 75, 75)
