from mindstorms import MSHub, MotorPair, ColorSensor

motor_pair = MotorPair('B', 'A')
color_sensor = ColorSensor('C')


def course_correction():
    """
    PID module.

    Calculate the light intensity and the rate of change.
    :return: an integer
    """
    global color_sensor
    porportinal_error = 9 - color_sensor.get_reflected_light()  # arbitrary placeholder
    integral_error = porportinal_error - color_sensor.get_reflected_light()
    derived_error = porportinal_error - color_sensor.get_reflected_light()

    return 5 * porportinal_error + 5 * integral_error + 5 * derived_error


while True:
    intensity = color_sensor.get_reflected_light()
    if intensity < 65:
        motor_pair.start(-10, -8)
        print('black')

    elif 72 < intensity < 90:
        motor_pair.start(0, -5)
        print('white')

    elif intensity > 90:
        motor_pair.stop()
        print('end')