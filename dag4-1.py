from time import perf_counter as pfc



def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    print(test)
    return test


def solve(puzzle):
    regels=puzzle.split('\n')
    for regel in regels:
        delen=regel.split(',')
        print(delen)
        a=delen[0].split('-')
        b=delen[1].split('-')
        print(a,b)


start=pfc()
print(solve(read_puzzle('dag4-test.txt')))
print(pfc()-start)