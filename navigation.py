from mindstorms import MSHub, MotorPair, ColorSensor, App

# Initialize the hub.
hub = MSHub()
# Initialize the motors connected to Ports A and B.
motor_pair = MotorPair('A', 'B')
# Initialize the Color Sensor connected to Port C.
color_sensor = ColorSensor('C')


def steer(light, tape, steer_range, light_range):
    """
    Normalize light values between light_range to values in steer_range.

    Ensure robot does not have heavy preference to right turns
    :param light: an integer that is the current amount of reflection from light sensor
    :param tape: an integer that is the amount of reflection from middle of black tape
    :param steer_range: an integer
    :param light_range: an integer
    :precondition light: must be an integer in the range [0,100]
    :precondition tape: must be an integer in the range [0,100]
    :precondition steer_range: must be an integer
    :precondition light_range: must be an integer
    :postcondition: will calculate a steer value as an integer and return it
    :return: a steer value to perform robot steering as an integer
    """
    return int(-95 + ((light - tape) * steer_range) / light_range)


def drive(tape, floor, steer_max):
    """
    A function to drive the robot on the right edge of black line.

    :param tape: an integer that is the reflection from middle of line
    :param floor: an integer that is the reflection from floor
    :param steer_max: an integer that is the max steer value
    :precondition tape: must be an integer in the range [0,100]
    :precondition floor: must be an integer in the range [0,100] and must be greater than tape parameter
    :precondition steer_max: must be an integer in the range [0,100]
    :precondition: a pair of motors to drive wheels are connected to hub
    :postcondition: robot will follow the black line
    :postcondition: lines detailing current light intensity and steer values are printed to the screen
    """
    steer_max_to_steer_min = steer_max - (-95)
    range_of_light_from_floor_to_tape = floor - tape

    while True:
        intensity = color_sensor.get_reflected_light()
        steer_value = steer(intensity, tape, steer_max_to_steer_min, range_of_light_from_floor_to_tape)
        if intensity <= (tape - 4):
            motor_pair.start_at_power(-38, (-1 * int(steer_value * 1.5)))
        else:
            motor_pair.start_at_power(40, steer)

        print('light sensor: {0}, turn value {1}'.format(intensity, steer))


drive(21, 75, 68)
