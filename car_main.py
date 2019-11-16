import RPi.GPIO as GPIO         # 引入GPIO模块
import time                     # 引入time模块

#left wheel
ENA = 13
IN1 = 19
IN2 = 26

#right wheel
ENB = 17
IN3 = 27
IN4 = 22

ServoPin = 24
PWMFreq = 500

time_node = 1

def init():
    print("start init.")
    clear()
    # 初始化
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(ServoPin, GPIO.OUT)              
    GPIO.setup(ENA, GPIO.OUT)           
    GPIO.setup(IN1, GPIO.OUT)           
    GPIO.setup(IN2, GPIO.OUT)     

    GPIO.setup(ENB, GPIO.OUT)           
    GPIO.setup(IN3, GPIO.OUT)           
    GPIO.setup(IN4, GPIO.OUT)

    print("end init.")

def reset():
    print("start reset.")
    GPIO.output(IN1, GPIO.LOW)        
    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)        
    GPIO.output(IN4, GPIO.LOW)
    print("end init.")


def forward():
    reset()
    GPIO.output(IN1, GPIO.LOW)        
    GPIO.output(IN2, GPIO.HIGH)

    GPIO.output(IN3, GPIO.HIGH)        
    GPIO.output(IN4, GPIO.LOW)

def back():
    reset()
    GPIO.output(IN1, GPIO.HIGH)        
    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.LOW)        
    GPIO.output(IN4, GPIO.HIGH)

def speedup(pmw_l,pwm_r):
    for i in range(0,10,1):
        time.sleep(0.3)
        pmw_l.ChangeDutyCycle(i*10)  
        pwm_r.ChangeDutyCycle(i*10) 

def slowdown(pmw_l,pwm_r):
    pmw_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)  

def trun_dir(num,pwm_turn):
    print("trun num= %s" % str(num))
    if num < 0 or num > 180:
        num = 90
    duty = (1/18) * num + 2.5   # 将角度转换为占空比
    pwm_turn.ChangeDutyCycle(duty)  
        


def clear():
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        init()

        print("start create pwm_wheel.")
        pwm_left = GPIO.PWM(ENA, PWMFreq)    
        pwm_right = GPIO.PWM(ENB, PWMFreq)
        pwm_left.start(0)     
        pwm_right.start(0)

        print("start create pwm_trun.")
        pwm_trun = GPIO.PWM(ServoPin, 50) 
        pwm_trun.start(0)

        trun_dir(90,pwm_trun)
  
   
        trun_dir(120,pwm_trun)
        forward()
        speedup(pwm_left,pwm_right)
        time.sleep(time_node)
        slowdown(pwm_left,pwm_right)

        back()
        speedup(pwm_left,pwm_right)
        time.sleep(time_node)
        slowdown(pwm_left,pwm_right)

        trun_dir(60,pwm_trun)
        forward()
        speedup(pwm_left,pwm_right)
        time.sleep(time_node)
        slowdown(pwm_left,pwm_right)

        back()
        speedup(pwm_left,pwm_right)
        time.sleep(time_node)
        slowdown(pwm_left,pwm_right)

        trun_dir(90,pwm_trun)
        time.sleep(1)

        pwm_left.stop()
        pwm_right.stop() 
        pwm_trun.stop()

        clear()  

    except Exception as e:
        print("e = " + str(e))
        clear()             

          
