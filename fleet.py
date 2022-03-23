

from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        
    def create_fleet(self):
        bot_1 = Robot('Optimus Prime')
        bot_2 = Robot('WALL-E')
        bot_3 = Robot('R2D2')
       
        self.robots.append(bot_1)
        self.robots.append(bot_2)
        self.robots.append(bot_3)
