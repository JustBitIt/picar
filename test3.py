import RPi.GPIO as GPIO         # 引入GPIO模块
import time                     # 引入time模块

ENA = 13
IN1 = 19
IN2 = 26

if __name__ == '__main__':
    try:
        # 初始化
        GPIO.setmode(GPIO.BCM)              
        GPIO.setup(ENA, GPIO.OUT)           
        GPIO.setup(IN1, GPIO.OUT)           
        GPIO.setup(IN2, GPIO.OUT)           

        freq = 500
        speed = 0
        pwm = GPIO.PWM(ENA, freq)           
        pwm.start(speed)                    

        while True:
            # 将电机设置为正向转动
            GPIO.output(IN1, False)        
            GPIO.output(IN2, True)   
            pwm.ChangeDutyCycle(100)     

            # # 通过改变PWM占空比，让电机转速不断加快
            # for speed in range(0, 100, 5):
            #     pwm.ChangeDutyCycle(speed)  
            #     time.sleep(1)

            # 将电机设置为反向转动
            # GPIO.output(IN1, True)          
            # GPIO.output(IN2, False)         

            # 通过改变PWM占空比，让电机转速不断加快
            # for speed in range(0, 100, 5):
            #     pwm.ChangeDutyCycle(speed)  
            #     time.sleep(1)
                
    finally:
        pwm.stop()                          
        GPIO.cleanup()                      
