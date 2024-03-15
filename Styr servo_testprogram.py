import threading
from time import sleep
from ServoControl import servo_control			#Importerar programkoden för att styra servon, via PCA9685




 
############################################# HUVUDPROGRAM ###############################################
"""encoder = RotaryEncoder() #Definierar IMU-avläsningen
encoder_thread = threading.Thread(target=encoder.start_encoder)
encoder_thread.start() #Startar IMU-avläsningen

while True:
    counter_value = encoder.get_counter()
    print("counter:", counter_value)
    sleep(0.1)"""

servo_control.servo_angle(0, 90)
    

    