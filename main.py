from mpi4py import MPI

import Genetic

size = 100
sizeOfRanges = 10

genetic = Genetic.Genetic()
genetic.initPopulation(size)
listOfRanges = genetic.dividePopulation(10)

comm = MPI.COMM_WORLD
rank = comm.rank

sizeOfPopulationPerProcess = (size // sizeOfRanges) // (comm.size - 1)

if rank == 0:
    # print('size of pop per node', sizeOfPopulationPerProcess)
    data1 = listOfRanges[:sizeOfPopulationPerProcess]
    data2 = listOfRanges[sizeOfPopulationPerProcess:]
    comm.send(data1, dest=1)
    comm.send(data2, dest=2)
    print('sending data from node', rank, 'to nodes 1,2')
    data1 = comm.recv(source=1)
    data2 = comm.recv(source=2)
    print('reciving data from 1,2')
elif rank == 1:
    data = comm.recv(source=0)
    print('reciving data from 0')
    genetic.runSingleStepOfAlghoritm(data)
    comm.send(data, dest=0)
    print('sending data from node', rank, 'to node 0')
elif rank == 2:
    data = comm.recv(source=0)
    print('reciving data from 0')
    genetic.runSingleStepOfAlghoritm(data)
    comm.send(data, dest=0)
    print('sending data from node', rank, 'to node 0')
