from pybricks.parameters import Color, Direction
from pybricks.media.ev3dev import ImageFile, Image

class LineFollower:
    def __init__(self, drivebase, color_sensor, ev3):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.ev3 = ev3 # for beeping and displaying
        self.running = False
        self.turnstate = "RIGHT"
        self.turned = 0
        self.searched_color = Color.RED


    def follow(self):
        print("running")
        self.running = True
        while self.running:
            print(self.color_sensor.color())
            self.ev3.light.on(self.color_sensor.color())
            if self.color_sensor.color() == self.searched_color:
                self.ev3.screen.load_image(ImageFile.FORWARD)
                self.drivebase.straight(100)
            else:
                self.ev3.speaker.beep() 
                self.search_line()


    def search_line(self):
        print("searching for line")
        self.turned = 0
        while self.color_sensor.color() != self.searched_color:
            if self.turnstate == "RIGHT":
                self.ev3.screen.load_image(ImageFile.RIGHT)
                self.drivebase.turn(10)
                self.turned += 10
                if self.turned >= 90:
                    self.ev3.screen.load_image(ImageFile.NO_GO)
                    self.drivebase.turn(-90)
                    self.turned = 0
                    self.turnstate = "LEFT"
            elif self.turnstate == "LEFT":
                self.ev3.screen.load_image(ImageFile.LEFT)
                self.drivebase.turn(-10)
                self.turned += 10
                if self.turned >= 90:
                    self.ev3.screen.load_image(ImageFile.NO_GO)
                    self.drivebase.turn(90)
                    self.turned = 0
                    self.turnstate = "RIGHT"
        print("found line")
        