from vex import *
import urandom
import time

# Initialize the brain and other components
brain = Brain()

# Set up the encoder, motor, and bumper
daencoder_a = Encoder(brain.three_wire_port.a)
damotor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
dabumper_c = Bumper(brain.three_wire_port.c)



while True:
    
    if dabumper_c.pressing():
        brain.program_stop()
    else:
        encoder_value = daencoder_a.velocity()
        motor_speed = encoder_value * 1 
        motor_speed = max(min(motor_speed, 256), -256)
        damotor_1.spin(FORWARD, motor_speed)

    
    
