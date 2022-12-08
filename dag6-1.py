from time import perf_counter as pfc

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    
    return test



def solve(puzzle):
    marker=False
    i=-1
    while not marker:
        i+=1
        if puzzle[i]!=puzzle[i+1] and puzzle[i]!=puzzle[i+2] and puzzle[i]!=puzzle[i+3]:
            if puzzle[i+1]!=puzzle[i+2] and puzzle[i+1]!=puzzle[i+3]:
                if puzzle[i+2]!=puzzle[i+3]:

                    marker=True
        print(puzzle[i],end="")
    return i+4


start=pfc()
print(solve(read_puzzle('dag6.txt')))
print(pfc()-start)