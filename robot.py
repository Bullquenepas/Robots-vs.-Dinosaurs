


from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon('Ion Blaster', 20)

    def attack(self, dinosaur):
        dino_opponent = dinosaur
        dino_opponent.health = dino_opponent.health - self.attack_power
        return dino_opponent.health