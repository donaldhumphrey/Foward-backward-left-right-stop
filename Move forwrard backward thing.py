def move_forward():
    Left_Motor_speed = 1 #Makes left wheel forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Makes right motor go forward
    Right_Motor.throttle = Right_Motor_speed

def move_backward():
    Left_Motor_speed = -1 #Makes left wheel backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Makes right motor go backward
    Right_Motor.throttle = Right_Motor_speed

def turn_left():
    Left_Motor_speed = -1 #Makes left wheel backward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 #Makes right motor go forward
    Right_Motor.throttle = Right_Motor_speed

def turn_right():
    Left_Motor_speed = 1 #Makes left wheel forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 #Makes right motor go backward
    Right_Motor.throttle = Right_Motor_speed

def stop():
    Left_Motor_speed = 0 #Makes left wheel forward
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 0 #Makes right motor go backward
    Right_Motor.throttle = Right_Motor_speed

