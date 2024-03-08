from pybricks.parameters import Color

class LineFollower:
    def __init__(self, drivebase, color_sensor, ev3, imagefile):
        self.drivebase = drivebase
        self.color_sensor = color_sensor
        self.ev3 = ev3 # for beeping and displaying
        self.imagefile = imagefile
        self.running = False
        self.searched_color = Color.YELLOW


    def follow(self):
        print("running")
        self.running = True
        while self.running:
            print(self.color_sensor.color())
            self.ev3.light.on(self.color_sensor.color())
            if self.color_sensor.color() == self.searched_color:
                self.ev3.screen.draw_image(source=self.imagefile.FORWARD, y=20, x=20)
                self.drivebase.straight(100)
            else:
                # stopping
                self.ev3.speaker.beep() 
                self.search_line()


    def search_line(self):
        print("searching for line")
        left, right = -20, 20
        angle = left
        while True:
            self.drivebase.turn(angle)
            if self.color_sensor.color() == self.searched_color:
                print("found line")
                break
            if angle > 90:
                self.ev3.screen.draw_image(source=self.imagefile.NO_GO, y=20, x=20)
                break
            if angle == right:
                self.ev3.screen.draw_image(source=self.imagefile.RIGHT, y=20, x=20)
                angle = left
                right += 10 - left
            elif angle == left:
                self.ev3.screen.draw_image(source=self.imagefile.LEFT, y=20, x=20)
                angle = right
                left -= 10 + right
