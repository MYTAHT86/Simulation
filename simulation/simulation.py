import os 
import time
import msvcrt

from wcwidth import wcswidth

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
    def render(cls) -> None:
        for row in Map.map:
            print(*((' ' * (4 - wcswidth(el)) + el for el in row)), sep=' ', end='\n\n')
        print(f"Количество проделанных ходов {Simulation.turns_count}")
        print()     
    
    @classmethod
    def next_turn(cls) -> None:
        for ex in (list(filter(lambda x: isinstance(x, Herbivore), Map.collection.values()))):
            ex.make_move()
        for ex in (list(filter(lambda x: isinstance(x, Predator), Map.collection.values()))):
            ex.make_move()   
        Simulation.turns_count += 1
    
    @classmethod
    def continue_simulation(cls) -> None:
        Simulation.simulating = True
    
    @classmethod
    def pause_simulation(cls) -> None:
        Simulation.simulating = False
        print('Симуляция приостановлена')
Simulation.init_actions = [MakeMap.activate, MakeDefaultWorld.activate]
Simulation.turn_actions = [Simulation.next_turn, CheckEcoSystem.activate, Simulation.render]