import time
import os 
import msvcrt

from simulation.simulation import Simulation

if __name__ == "__main__":
    print("Добро пожаловать в симуляцию животного мира. В ходе симуляции вы можете остановить процесс, нажав на Пробел")
    os.system("cls")
    for action in Simulation.init_actions:
        action()
    Simulation.render()
    time.sleep(2)
    while not Simulation.break_status:
        if Simulation.simulating:
            os.system("cls")
            for action in Simulation.turn_actions:
                action()
        time.sleep(2)
        if msvcrt.kbhit():
            user_input = msvcrt.getch()
            if user_input == b'p':
                Simulation.pause_simulation()
            elif user_input == b'c':
                Simulation.continue_simulation()
            elif user_input == b'e':
                Simulation.break_status = True
    print("Симуляция закончена")
    
