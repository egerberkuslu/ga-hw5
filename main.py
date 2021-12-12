# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Instance import Instance
import random

from PBIL import PBIL


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    problems  = ["instances_01_KP/large_scale/knapPI_1_100_1000_1", "large_scale/knapPI_1_200_1000_1",
                  "large_scale/knapPI_1_500_1000_1",
                  "large_scale/knapPI_1_1000_1000_1", "large_scale/knapPI_1_2000_1000_1",
                  "large_scale/knapPI_1_5000_1000_1", "large_scale/knapPI_1_10000_1000_1"]


    optimums = ["instances_01_KP/large_scale-optimum/knapPI_1_100_1000_1", "large_scale-optimum/knapPI_1_200_1000_1",
                  "large_scale-optimum/knapPI_1_500_1000_1",
                  "large_scale-optimum/knapPI_1_1000_1000_1", "large_scale-optimum/knapPI_1_2000_1000_1",
                  "large_scale-optimum/knapPI_1_5000_1000_1", "large_scale-optimum/knapPI_1_10000_1000_1"]

    instance = Instance(problems[0],optimums[0])
    gen = random.randint(0,1000) + 500
    popSize = random.randint(0,400) + 200
    truncSel = random.choice([True, False])
    pbil = PBIL()
    best = pbil.run(popSize, gen, 0.1 , popSize//5 , False, instance)
    print("Fitness", best.getFitness())
    print("Weight", best.getWeight())
    print("Genes", best.print())
    print("Iteration", pbil.getGeneration() , " generations")

