from time import perf_counter as pfc

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
        print(test)
    return test


def solve(puzzle):
    lines= puzzle.split('\n')
    print (lines)

    cycle=0
    X=1
    cycles=[1]

    for line in lines:
        parts = line.split()
        print(parts)
        if parts[0]=='noop':
            cycles.append(X)
        else:
            plus=int(parts[1])
            print(plus)
            cycles.append(X)
            cycles.append(X)
            X+=plus
    print(cycles[0:20])
    #print (cycles[20],cycles[60],cycles[100],cycles[140],cycles[180],cycles[220])
    return cycles[20]*20+cycles[60]*60+cycles[100]*100+cycles[140]*140+cycles[180]*180+cycles[220]*220



    
    

    return None

        



start=pfc()
print(solve(read_puzzle('dag10-test.txt')))
print(pfc()-start)