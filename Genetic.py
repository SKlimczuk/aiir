import random
import math
import Gen

class Genetic:
    population = []

    def generateRandomPopulationSize(self):
        generatedRadnomNumber = random.randint(100, 1000)
        return generatedRadnomNumber

    def initRandomPopulation(self):
        for i in range(self.generateRandomPopulationSize()):
            gen = Gen.Gen(i)
            self.population.append(gen)

    def initPopulation(self, limit):
        for i in range(limit):
            gen = Gen.Gen(i)
            self.population.append(gen)

    def dividePopulation(self, limit):
        if len(self.population):
            ranges = []
            sizeOfPopulation = len(self.population)
            ammountOfRanges = sizeOfPopulation // limit
            for i in range(ammountOfRanges):
                start = i * limit
                stop = i * limit + limit
                tempRange = self.population[start:stop]
                ranges.append(tempRange)
            return ranges
        else:
            print("Population is not initialized !")

    # ---------------------------------------------------- this will be the part to do on nodes
    def mutate(self, listToMutate):
        genA = Gen.Gen(0)
        size = len(listToMutate)
        a = random.randint(0, size - 1)
        b = random.randint(0, size - 1)
        genA = listToMutate[a]
        genB = listToMutate[b]
        mutatedAdaptation = genA.mutation(genB)
        mutant = Gen.Gen(random.randint(1000000, 10000000))
        mutant.set_adaptation(mutatedAdaptation)
        listToMutate.append(mutant)
        return listToMutate

    def ranking(self, listToRank):
        self.mutate(listToRank)
        sizeOfListToRank = len(listToRank)
        for i in range(sizeOfListToRank):
            for j in range(0, sizeOfListToRank - i - 1):
                if listToRank[j] > listToRank[j + 1]:
                    listToRank[j], listToRank[j + 1] = listToRank[j + 1], listToRank[j]
        return listToRank[:sizeOfListToRank - 1]

    def runSingleStepOfAlghoritm(self, population):
        size = len(population)
        for i in range(size):
            self.ranking(population[i])
