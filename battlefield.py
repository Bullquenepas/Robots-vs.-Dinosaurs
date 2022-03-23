

from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
       self.fleet = Fleet()
       self.herd = Herd()

def run_game(self):
    self.fleet.create_fleet()
    self.herd.create_herd()
    self.display_welcome()
    self.battle()

def display_welcome(self):
    print('Welcome to Robots vs Dinosaurs')
    for robot in self.fleet.robots:
        print(f"{robot.name} - Health Points: {robot.health} Equipped Weapon: {robot.weapon.name} Weapon Attack Power: {robot.weapon.attack_power}")

    for dino in self.herd.dinosaurs:
        print(f"{dino.name} - Health Points: {dino.health} Weapon Attack Power: {dino.attack_power}")

#cant decide how to conduct fight! Re doing - ran out of time.
def battle(self):
    pass

def dino_turn(self, dinosaur):
    pass

def robo_turn(self):
    pass

def show_dino_opponent_options(self):
    pass

def show_robo_opponent_options(self):
    pass

def show_winners(self):
    pass