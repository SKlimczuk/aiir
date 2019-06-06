from mpi4py import MPI
import sys
import Genetic

# size = int(sys.argv[1])
size = 100
sizeOfRanges = 10
generations = 5

genetic = Genetic.Genetic()
genetic.initPopulation(size)
listOfDividedPopulations = genetic.dividePopulation(10)

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
    data1 = comm.recv(source=1)
    data2 = comm.recv(source=2)
    if genetic.calcAdaptation(data1) > genetic.calcAdaptation(data2):
        print(data1)
    else:
        print(data2)
else:
    print('slave rank', rank, ', with name', name)
    data = comm.recv(source=0)
    data = genetic.runAlgorithm(data, generations)
    comm.send(data, dest=0)