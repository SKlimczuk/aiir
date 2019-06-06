from mpi4py import MPI
import Genetic

size = 100
sizeOfRanges = 10
generations = 5

genetic = Genetic.Genetic()
genetic.initPopulation(size)
listOfDividedPopulations = genetic.dividePopulation(10)

# genetic.findTheStrongestPopulation(listOfDividedPopulations)

comm = MPI.COMM_WORLD
rank = comm.rank
name = MPI.Get_processor_name()

sizeOfPopulationPerProcess = (size // sizeOfRanges) // (comm.size - 1)

if rank == 0:
    data1 = listOfDividedPopulations[:sizeOfPopulationPerProcess]
    data2 = listOfDividedPopulations[sizeOfPopulationPerProcess:]
    comm.send(data1, dest=1)
    comm.send(data2, dest=2)
    print('root rank', rank, ', with name', name)
    genetic.findTheStrongestPopulation(listOfDividedPopulations)
else:
    print('slave rank', rank, ', with name', name)
    data = comm.recv(source=0)
    genetic.runAlgorithm(data, generations)
    # for x in range(len(data)):
    #     print(data[x])
    # comm.send(data, dest=0)
    comm.gather(data, root=0)

# elif rank == 1:
#     data = comm.recv(source=0)
#     genetic.runSingleStepOfAlghoritm(data)
#     comm.send(data, dest=0)
# elif rank == 2:
#     data = comm.recv(source=0)
#     genetic.runSingleStepOfAlghoritm(data)
#     comm.send(data, dest=0)
