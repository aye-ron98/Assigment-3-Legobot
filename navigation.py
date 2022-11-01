from mindstorms import MSHub, MotorPair, ColorSensor


def course_correction():
    """
    Calculate course correction scalar.

    Function to examine the difference between centerline black and current position. Will return an integer to be used
    to scale motor speed.
    :return: an integer
    """
    color_sensor = ColorSensor('C')
    porportinal_error = 65 - color_sensor.get_reflected_light()  # arbitrary placeholder
    return 0.5 * porportinal_error


def drive(speed):
    """
    Drives robot.

    A function to drive the robot on the black line
    :param speed: integer between [1, 100]
    :precondition: speed must be an integer between [1, 100]
    :postconidion: wheel motors will move at rotation rate equivalent to speed
    """
    while True:
        motor_pair = MotorPair('B', 'A')
        intensity = ColorSensor('C').get_reflected_light()

        if intensity < 54:
            motor_pair.start(speed - course_correction(), speed + course_correction())
            print('correct right')
        elif 55 < intensity < 65:
            motor_pair.start(speed, speed)
            print('straight')
        elif intensity > 66:
            motor_pair.start(speed + course_correction(), speed - course_correction())
            print('correct left')
        elif intensity > 90:
            motor_pair.stop()
            print('end')


drive(30)
