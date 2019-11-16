import RPi.GPIO as GPIO                 # 引入GPIO模块  
import time                             # 引入time模块  

GPIO.setmode(GPIO.BCM)                  # 使用BCM编号方式  

GPIO.setup(19, GPIO.OUT)                # 将GPIO19设置为输出模式  

if __name__ == '__main__':
    try:
        while True:                     # 无限循环  
            GPIO.output(19, True)       # 将GPIO19设置为高电平，点亮LED  
            time.sleep(1)               # 等待1秒钟  
            GPIO.output(19, False)      # 将GPIO19设置为低电平，熄灭LED  
            time.sleep(1)               # 等待1秒钟  
    finally:
        GPIO.cleanup()                  # 清理释放GPIO资源，将GPIO复位  
