

class Instance:

    def __init__(self, problem:str, optimum:str):
        self.n = 0
        self.capacity = 0
        self.targetFitness = 0
        self.profit = []
        self.weight = []
        self.readData(problem, optimum)


    def readData(self,problem, optimum):
        print(problem)
        self.profit = []
        self.weight = []
        with open(problem) as f:
            self.n, self.capacity = [int(x) for x in next(f).split()]
            all_data = [[int(x) for x in line.split()] for line in f]

        for i in range(self.n):
            self.profit.append((all_data[i][0]))
            self.weight.append(all_data[i][1])


        with open(optimum) as f:
            self.targetFitness = [int(x) for x in next(f).split()][0]

        print("N", self.n)
        print("CAPACITY", self.capacity)
        print("Profits", self.profit)
        print("Weights", self.weight)
        print("Target Fitness", self.targetFitness)

    def getWeight(self,index):
        return self.weight[index]

    def getProfit(self,index):
        return self.profit[index]

    def getNItems(self):
        return self.n

    def getCapacity(self):
        return self.capacity

    def getTargetFitness(self):
        return self.targetFitness