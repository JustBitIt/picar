import RPi.GPIO as GPIO                 # 引入GPIO模块

if __name__ == '__main__':
    LedPin = 19
    freq = 100                          # 存放PWM频率变量，这里初始值为100，可以根据实际需要修改
    dc = 0                              # 存放PWM占空比变量，这里初始值为0，可以根据实际需要修改

    GPIO.setmode(GPIO.BCM)              # 使用BCM编号方式
    GPIO.setup(LedPin, GPIO.OUT)        # 将GPIO19设置为输出模式

    pwm = GPIO.PWM(LedPin, freq)        # 创建PWM对象，并指定初始频率
    pwm.start(dc)                       # 启动PWM，并指定初始占空比

    try:
        freq = int(input("Please input the frequency of PWM(1-2000Hz): "))  # 等待输入新PWM频率
        pwm.ChangeFrequency(freq)       # 改变PWM频率
        while True:
            dc = int(input("Please input the duty cycle(0-100): "))         # 等待输入新PWM占空比
            pwm.ChangeDutyCycle(dc)     # 改变PWM占空比
    finally:
        pwm.stop()                      # 停止PWM
        GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位