from mpi4py import MPI
import sys
import Genetic

size = int(sys.argv[1])
generations = int(sys.argv[2])

sizeOfRanges = 10

genetic = Genetic.Genetic()
genetic.initPopulation(size)
listOfDividedPopulations = genetic.dividePopulation(sizeOfRanges)

comm = MPI.COMM_WORLD
rank = comm.rank
name = MPI.Get_processor_name()

sizeOfPopulationPerProcess = (size // sizeOfRanges) // (comm.size - 1)

if rank == 0:
    print('root rank', rank, ', with name', name)
    amountOfNodes = comm.size - 1

    dataList = []
    for x in range(amountOfNodes):
        begin = x * sizeOfPopulationPerProcess
        end = (x + 1) * sizeOfPopulationPerProcess
        dataList.append(listOfDividedPopulations[begin:end])

    counter = 0
    for data in dataList:
        counter += 1
        comm.send(data, dest=counter)

    highestAdaptation = 0
    strongestPopulation = 0
    populationToCompare = 0

    counter = 0
    for x in range(amountOfNodes):
        counter += 1
        populationToCompare = comm.recv(source=counter)
        if genetic.calcAdaptation(populationToCompare) >= highestAdaptation:
            strongestPopulation = populationToCompare
            highestAdaptation = genetic.calcAdaptation(strongestPopulation)
else:
    print('slave rank', rank, ', with name', name)
    data = comm.recv(source=0)
    data = genetic.runAlgorithm(data, generations)
    comm.send(data, dest=0)
