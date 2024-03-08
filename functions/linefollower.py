from pybricks.parameters import Color

class LineFollower:
    def __init__(self, drivebase, color_sensor, ev3):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.ev3 = ev3 # for beeping and displaying
        self.running = False
        self.searched_color = Color.YELLOW


    def follow(self):
        print("running")
        self.running = True
        while self.running:
            print(self.color_sensor.color())
            if self.color_sensor.color() == self.searched_color:
                self.drivebase.straight(100)
            else:
                # stopping
                self.ev3.speaker.beep() 
                self.search_line()
                self.running = False


    def search_line(self):
        print("searching for line")
        # searching methode here
        if self.color_sensor.color() == self.searched_color:
            print("found line")
            self.running = True
            