import random
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

        return self.population

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
                if listToRank[j] < listToRank[j + 1]:
                    listToRank[j], listToRank[j + 1] = listToRank[j + 1], listToRank[j]
        return listToRank[:10]

    def runAlgorithm(self, population, generations):
        sizeOfPopulation = len(population)
        for g in range(generations):
            for i in range(sizeOfPopulation):
                self.ranking(population[i])
                population[i] = self.ranking(population[i])
        result = self.findTheStrongestPopulation(population)
        return result

    def findTheStrongestPopulation(self, populations):
        strongest = 0
        strongestPopulation = 0
        for p in populations:
            candidate = self.calcAdaptation(p)
            if candidate >= strongest:
                strongest = candidate
                strongestPopulation = p
        return strongestPopulation

    def calcAdaptation(self, population):
        gen = Gen.Gen(0)
        sizeOfPopulation = len(population)
        sum = 0
        for i in range(sizeOfPopulation):
            gen = population[i]
            sum += gen.get_adaptation()
        return sum

    def printResultToFile(self, result):
        file = open('result', 'w')
        for line in result:
            lineToWrite = str(line)
            file.writelines(lineToWrite + "\n")
        file.close()
