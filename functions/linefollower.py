from pybricks.parameters import Color

class LineFollower:
    def __init__(self, drivebase, color_sensor):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.running = False

    def follow(self):
        print("running")
        self.running = True
        while self.running:
            print(self.color_sensor.color())
            if self.color_sensor.color == Color.BLACK:
                self.drivebase.drive(100, 100)
            else:
                pass
                # self.drivebase.drive(-100, -100)