import random

from Instance import Instance
import sys

class Genome:

    def __init__(self, instance: Instance):
        self.fitnessMode = "Repair"
        self.weight = 0
        self.profit = 0
        self.penaltyValue = 10
        self.changed = False
        self.genes = [False] * instance.getNItems()
        for i in range(len(self.genes)):
            if random.uniform(0,1) < 0.5:
                if self.weight + instance.getWeight(i) <= instance.getCapacity():
                    self.genes[i] = True
                    self.weight = self.weight + instance.getWeight(i)
                    self.profit = self.profit + instance.getProfit(i)

        self.instance = instance

    def setFitnessMode(self, fitnessMode):
        self.fitnessMode = fitnessMode

    def setPenaltyValue(self, value):
        self.penaltyValue = value

    def getWeight(self):
        return self.weight

    def getGene(self,index):
        return self.genes[index]


    def getFitness(self):
        if self.changed:
            self.profit = 0
            self.weight = 0
            for i in range(self.instance.getNItems()):
                if self.getGene(i):
                    self.profit = self.profit + self.instance.getProfit(i)
                    self.weight = self.weight + self.instance.getWeight(i)

        if self.weight > self.instance.getCapacity():
            if self.fitnessMode == "Regular":
                return self.profit
            if self.fitnessMode == "DeathPenalty":
                return sys.minint
            if self.fitnessMode == "Penalty":
                return self.profit - (self.weight - self.instance.getCapacity()) * self.penaltyValue
            if self.fitnessMode == "Repair":
                while self.weight > self.instance.getCapacity():
                    index = random.randint(0,len(self.genes)-1)
                    if self.getGene(index):
                        self.genes[index] = False
                        self.weight = self.weight - self.instance.getWeight(index)
                        self.profit = self.profit - self.instance.getProfit(index)

        return self.profit

    def getSize(self):
        return len(self.genes)

    def setGene(self,index, value):
        self.genes[index] = value
        self.changed = True

    def flipGene(self,index):
        self.genes[index] = not self.genes[index]
        self.changed = True

    def print(self):
        out = ""
        for gene in self.genes:

            if gene:
                out = out + "1"
            else:
                out = out + "0"
        print(out)

    def isBetter(self,rhs):
        if self.isFeasible() and rhs.isFeasible():
            return self.profit > rhs.profit
        if  not self.isFeasible() and  not rhs.isFeasible():
            return (self.weight - self.instance.getCapacity()) < (rhs.weight - self.instance.getCapacity())

        return self.isFeasible()

    def __lt__(self, SecondGenome):
        return SecondGenome.getFitness() - self.getFitness()

    def isFeasible(self):
        self.getFitness()
        return self.weight <= self.instance.getCapacity()