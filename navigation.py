from mindstorms import MSHub, MotorPair, ColorSensor

motor_pair = MotorPair('A', 'B')
color_sensor = ColorSensor('C')


def course_correction():
    """
    PID module.

    Calculate the light intensity and the rate of change.
    :return: an integer
    """
    global color_sensor
    porportinal_error = 2500 - color_sensor.get_reflected_light()  # arbitrary placeholder
    integral_error = porportinal_error - color_sensor.get_reflected_light()
    derived_error = porportinal_error - color_sensor.get_reflected_light()

    return 5 * porportinal_error + 5 * integral_error + 5 * derived_error


def navigate_car():
    """
    Drive car
    :return: position
    """
    global motor_pair
    global color_sensor

    while True:
        intensity = color_sensor.get_reflected_light()
        if intensity == 2500:
            motor_pair.start(30 - course_correction(), 25 + course_correction())
            print('black')
        elif intensity != 2500:
            motor_pair.start(0, 25 + course_correction())
            print('white')
        elif intensity < 30:
            motor_pair.stop()
            print('end')

while True:
    color = color_sensor.wait_for_new_color()
    if color == 'black':
        motor_pair.start(0, 30)
        print('black')
    elif color == 'white':
        motor_pair.stop()
        print('white')