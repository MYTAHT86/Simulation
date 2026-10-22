from wcwidth import wcswidth
import os 
import time
import msvcrt
from map.map import Map
from creatures.herbivore import Herbivore
from creatures.predator import Predator
from makers.makemap import MakeMap
from makers.makedefaultworld import MakeDefaultWorld
from checkecosystem.checkecosystem import CheckEcoSystem
class Simulation:
    simulating = True
    turns_count = 0
    break_status = False
    @classmethod
    def render(cls):
        for row in Map.map:
            print(*((' ' * (4 - wcswidth(el)) + el for el in row)), sep=' ', end='\n\n')
        print(f"Количество проделанных ходов {Simulation.turns_count}")
        print()     
    @classmethod
    def next_turn(cls):
        os.system("cls")
        for ex in Herbivore.obj_collection:
            ex.make_move()
        for ex in Predator.obj_collection:
            ex.make_move()   
        Simulation.turns_count += 1
        Simulation.render()
        time.sleep(2)
    @classmethod
    def continue_simulation(cls):
        Simulation.simulating = True
    @classmethod
    def pause_simulation(cls):
        Simulation.simulating = False
        print('Симуляция приостановлена')
Simulation.init_actions = [MakeMap, MakeDefaultWorld]
Simulation.turn_actions = [Simulation.render, Simulation.next_turn, CheckEcoSystem.activate]