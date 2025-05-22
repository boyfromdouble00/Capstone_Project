import RPi.GPIO as GPIO
import time

# 핀 번호 설정
IN3 = 27
IN4 = 22


# GPIO 초기화
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

try:
    while True:
        print("💧 가습기 ON (5초)")
        # 정방향 회전 (OUT4: + / OUT3: -)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(5)

        print("💤 가습기 OFF (10초)")
        # 정지
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        time.sleep(3)

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    GPIO.cleanup()

