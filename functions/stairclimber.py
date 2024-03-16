from pybricks.tools import wait
from pybricks.media.ev3dev import SoundFile

class StairClimber:
    
    def __init__(self, ev3, drivebase, touch_sensor, lift_motor, rear_motor):
        self.ev3 = ev3
        self.drivebase = drivebase
        self.touch_sensor = touch_sensor
        self.lift_motor = lift_motor
        self.rear_motor = rear_motor
        self.running = False
        self.steps = 0
        
        rear_motor.dc(-20)
        lift_motor.dc(100)
        while not touch_sensor.pressed():
            wait(10)
        lift_motor.dc(-100)
        rear_motor.dc(40)
        wait(50)
        lift_motor.run_angle(-145, 510)
        rear_motor.hold()
        lift_motor.run_angle(-30, 44)
        lift_motor.reset_angle(0)
        gyro_sensor.reset_angle(0)
        
    def climb(self, steps):
        self.ev3.speaker.say("Klettern gestartet")
        self.steps = steps
        self.running = True
        self.ev3.screen.draw_text(70, 50, steps)
        self.drivebase.stop()
        while self.running and self.steps > 0:
            self.ev3.speaker.say("Nächste Stuffe")
            
            self.drivebase.straight(100)
            self.rear_motor.dc(90)
            wait(10)
            
            # TODO Find Logic to stop driving to wall
            
            self.lift_motor.dc(90)
            self.drivebase.straight(30)
            self.rear_motor.dc(15)
            
            while not self.touch_sensor.pressed():
                wait(10)
            self.lift_motor.hold()
            
            self.drivebase.straight(60)    
            self.rear_motor.dc(100)  
            wait(1300)
            
            self.ev3.speaker.play_file(SoundFile.AIR_RELEASE)
            self.drivebase.straight(30)
            self.rear_motor.dc(30)
            self.lift_motor.run_target(160, 0)
            
            self.steps -= 1
            self.ev3.screen.clear()
            self.ev3.screen.draw_text(70, 50, steps)
        
        self.drivebase.straight(100)
        self.rear_motor.dc(90)
        wait(2000)
        self.drivebase.stop()
        self.rear_motor.hold()
        wait(5000)  
              