from mindstorms import MSHub, MotorPair, ColorSensor, Motor

motor_pair = MotorPair('B', 'A')
color_sensor = ColorSensor('C')


# def course_correction():
#     """
#     PID module.

#     Calculate the light intensity and the rate of change.
#     :return: an integer
#     """
#     global color_sensor
#     porportinal_error = 9 - color_sensor.get_reflected_light() # arbitrary placeholder
#     integral_error = porportinal_error - color_sensor.get_reflected_light()
#     derived_error = porportinal_error - color_sensor.get_reflected_light()

#     return 5 * porportinal_error + 5 * integral_error + 5 * derived_error

# while True:
#     intensity = color_sensor.get_reflected_light()
#     if intensity < 65:
#         motor_pair.start(-10, -8)
#         print('straight')

#     elif 72 < intensity < 90:
#         motor_pair.start(0, -5)
#         print('correct')

#     elif intensity > 97 :
#         motor_pair.stop()
#         print('end')

# from mindstorms import MSHub, MotorPair, ColorSensor


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
    porportinal_error = (13 - light_offset)  # arbitrary placeholder
    return int(0.8 * porportinal_error)


# def drive(speed):
#     """
#     Drives robot.

#     A function to drive the robot on the black line
#     :param speed: integer between [1, 100]
#     :precondition: speed must be an integer between [1, 100]
#     :postconidion: wheel motors will move at rotation rate equivalent to speed
#     """
#     while True:
#         motor_pair = MotorPair('A', 'B')
#         intensity = ColorSensor('C').get_reflected_light()

#         if intensity < 10:
#             motor_pair.move_tank(10, 'cm', 30, 0)
#             # motor_pair.start(90, speed)
#             print(course_correction(intensity))
#         elif 20 < intensity < 35:
#             motor_pair.start(0, speed)
#             print('straight')
#         elif 36 < intensity < 40:
#             motor_pair.move_tank(10, 'cm', 0, 30)
#             # motor_pair.start(-course_correction(intensity), speed)
#             print(course_correction(intensity))
#         elif intensity > 41:
#             motor_pair.stop()
#             print(course_correction(intensity))


# drive(30)

def drive(speed):
    """
    Drives robot.

    A function to drive the robot on the black line
    :param speed: integer between [1, 100]
    :precondition: speed must be an integer between [1, 100]
    :postconidion: wheel motors will move at rotation rate equivalent to speed
    """
    while True:
        motor_right = Motor('B')
        motor_left = Motor('A')
        motor_pair = MotorPair('A', 'B')
        intensity = ColorSensor('C').get_reflected_light()

        if intensity < 8:
            motor_pair.move_tank(10, 'cm', 30, 0)
            # motor_pair.start(90, speed)
            print(course_correction(intensity))
        elif 9 < intensity < 19:
            motor_right.start(speed)
            motor_left.start(-speed)
            print('straight')
        elif 20 < intensity < 40:
            motor_pair.move_tank(10, 'cm', 0, 30)
            # motor_pair.start(-course_correction(intensity), speed)
            print(course_correction(intensity))
        elif intensity > 41:
            motor_pair.stop()
            print(course_correction(intensity))


drive(30)







