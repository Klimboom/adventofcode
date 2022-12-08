from time import perf_counter as pfc

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
        print(test)
    return test


def solve(puzzle):
    begin=0
    hulp=set()
    found=False
    while  not found:
        for i in range(14):
            hulp.add(puzzle[begin+i])
        if len(hulp)==14:
            found=True
        else:
            begin+=1
            hulp.clear()

    return begin+14

        



start=pfc()
print(solve(read_puzzle('dag6.txt')))
print(pfc()-start)