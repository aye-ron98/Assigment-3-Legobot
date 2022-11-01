from mindstorms import MSHub, MotorPair, ColorSensor


def course_correction(light_offset):
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
    porportinal_error = 65 - light_offset  # arbitrary placeholder
    return int(0.5 * porportinal_error)


def drive(speed):
    """
    Drives robot.

    A function to drive the robot on the black line
    :param speed: integer between [1, 100]
    :precondition: speed must be an integer between [1, 100]
    :postconidion: wheel motors will move at rotation rate equivalent to speed
    """
    while True:
        motor_pair = MotorPair('A', 'B')
        intensity = ColorSensor('C').get_reflected_light()

        if intensity < 54:
            motor_pair.start(speed + course_correction(intensity), speed - course_correction(intensity))
            print('correct right')
        elif 55 < intensity < 65:
            motor_pair.start(speed, speed)
            print('straight')
        elif intensity > 66:
            motor_pair.start(speed - course_correction(intensity), speed + course_correction(intensity))
            print('correct left')
        elif intensity > 90:
            motor_pair.stop()
            print('end')


drive(30)
