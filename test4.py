import RPi.GPIO as GPIO                 # 引入GPIO模块

if __name__ == '__main__':
    ServoPin = 18
    PWMFreq = 50                        # PWM信号频率

    GPIO.setmode(GPIO.BCM)              # 使用BCM编号方式
    GPIO.setup(ServoPin, GPIO.OUT)      
    pwm = GPIO.PWM(ServoPin, PWMFreq)   # 创建PWM对象，并设置频率为50
    pwm.start(0)                        # 启动PWM，并设置初始占空比0

    try:
        while True:
            # 等待输入一个0到180的角度
            direction = float(input("Pleas input the direction: "))
            if direction < 0 or direction > 180:
                print("Please input a direction between 0 an 180.")
                continue

            duty = (1/18) * direction + 2.5   # 将角度转换为占空比
            pwm.ChangeDutyCycle(duty)         # 改变PWM占空比
    finally:
        pwm.stop()                      # 停止PWM
        GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位





