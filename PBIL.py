import copy
import operator
import random

from Genome import Genome





class PBIL:
    def __init__(self):
        self.distributions = []

    def run(self, populationSize, generationCount, alpha, selectionSize, useTruncationSelection, instance):
        self.distributions = [0.5] * instance.getNItems()
        bestGenome = None
        self.population = []
        self.generation = 0
        for self.generation in range(generationCount):
            self.generatePopulation(populationSize, self.distributions, instance)
            bestChild = self.findBest(self.population)

            if bestGenome == None:
                bestGenome = bestChild
            elif bestChild.isBetter(bestGenome):
                bestGenome = bestChild

            if bestGenome.getFitness() == instance.getTargetFitness():
                break

            if useTruncationSelection:
                self.population = self.truncationSelection(selectionSize)
            else:
                self.population = self.tournamentSelection(selectionSize, selectionSize)

            self.updateDistributions(self.distributions, alpha, instance)

        return bestGenome

    def generatePopulation(self, populationSize, distributions, instance):
        self.population = [None] * populationSize
        for i in range(populationSize):
            genome = Genome(instance)
            for j in range(instance.getNItems()):
                if random.uniform(0, 1) < distributions[j]:
                    genome.setGene(j, True)
                else:
                    genome.setGene(j, False)

            self.population[i] = genome

    def findBest(self, population):
        best = population[0]
        for genome in population:
            if genome.isBetter(best):
                best = genome
        return best

    def truncationSelection(self, selectionSize):


        self.population = sorted(self.population, key=operator.attrgetter('profit'))

        truncated = copy.deepcopy(self.population)[:selectionSize]
        return truncated

    def tournamentSelection(self, selectionSize, tournamentSize):
        truncated = [None] * selectionSize
        for i in range(selectionSize):
            index = random.randint(0,len(self.population)-1)
            bestCandidate = self.population[index]
            for j in range(tournamentSize-1):
                index =  random.randint(0,len(self.population)-1)
                curr = self.population[index]
                if curr.getFitness() > bestCandidate.getFitness():
                    bestCandidate = curr
            truncated[i] = bestCandidate

        return truncated

    def updateDistributions(self, distributions, alpha, instance):
        for i in range(instance.getNItems()):
            count = 0
            for genome in self.population:
                if genome.getGene(i):
                    count = count + 1

            frequency = count / len(self.population)

            distributions[i] = (1-alpha) * distributions[i] + alpha * frequency

    def getGeneration(self):
        return self.generation