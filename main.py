import random
from wcwidth import wcswidth
import os 
import time
import msvcrt
random.seed(67)
from entity.entity import Entity
from static_objects.static_objects import Rock, Tree
from grass.grass import Grass
from creatures.creature import Creature
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from map.map import Map
from makers.makemap import MakeMap   
from makers.makemapobjects import MakeMapObjects
from makers.makedefaultworld import MakeDefaultWorld
from checkecosystem.checkecosystem import CheckEcoSystem
from simulation.simulation import Simulation

if __name__ == "__main__":
    print("Добро пожаловать в симуляцию животного мира. В ходе симуляции вы можете остановить процесс, нажав на Пробел")
    for action in Simulation.init_actions:
        action()
    while Simulation.break_status == False:
        if Simulation.simulating:
            for action in Simulation.turn_actions:
                action()
        if msvcrt.kbhit():
            user_input = msvcrt.getch()
            if user_input == b'p':
                Simulation.pause_simulation()
            elif user_input == b'c':
                Simulation.continue_simulation()
            elif user_input == b'e':
                Simulation.break_status = True
    print("Симуляция закончена")
    print("До скорых встреч ребятки")
