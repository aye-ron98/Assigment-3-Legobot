from mindstorms import MSHub, MotorPair, ColorSensor, App

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')


def scale(light, tape, steer_range, light_range):
    """
    Normalize light values between steer range to ensure robot does not have preference to right turns.

    :param light: an integer that is the amount from light sensor
    :param tape: an integer that is the amount of reflection from middle of black tape
    :param steer_range: an integer
    :param light_range: an integer
    :precondition: light must be an integer in the range [0,100]
    :precondition: tape must be an integer in the range [0,100]
    :precondition: steer_range must be an integer
    :precondition: light_range must be an integer
    :postcondition: will calculate steer value as an integer and return it
    :return: a steer value to correct steering as an integer
    """
    return int(-95 + ((light - tape) * steer_range) / light_range)


def drive(tape, floor, steer_max):
    """
    A function to drive the robot on the black line.

    :param tape: an integer that is the reflection from middle of line (lower bound)
    :param floor: an integer that is the reflection from floor (upper bound)
    :param steer_max: an integer that is the max steer value
    :precondition: tape is an integer in the range [0,100]
    :precondition: floor is an integer in the range [0,100] and must be greater than tape parameter
    :precondition: steer_max is an integer in the range [0,100]
    :postcondition: robot will follow the black line
    """
    steer_range = steer_max - (-95)
    light_range = floor - tape

    while True:
        intensity = color_sensor.get_reflected_light()
        steer = scale(intensity, tape, steer_range, light_range)
        if intensity <= (tape - 4):
            motor_pair.start_at_power(-38, (-1 * int(steer * 1.5)))
        else:
            motor_pair.start_at_power(40, steer)

        print('light sensor: {0}, turn value {1}'.format(intensity, steer))


drive(21, 75, 68)
