

from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        dino_1 = Dinosaur('The Sharptooth', 110)
        dino_2 = Dinosaur('Littlefoot', 60)
        dino_3 = Dinosaur('Spike', 75)

        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)