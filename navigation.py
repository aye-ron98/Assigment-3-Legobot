from mindstorms import MSHub, MotorPair, ColorSensor

motor_pair = MotorPair('B', 'A')
color_sensor = ColorSensor('C')

while True:
    color = color_sensor.wait_for_new_color()
    if color == 'black':
        motor_pair.start(0, 30)
        print('black')
    elif color == 'white':
        motor_pair.stop()
        print('white')