from time import perf_counter as pfc

hulp=[i for i in range(240)]
hulp.insert(0,-1)

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
    output=[]
    for i in range(1,41):
        if hulp[i]==cycles[i] or hulp[i]==cycles[i]-1 or hulp[i]==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    for i in range(40,80):
        if hulp[i]%40==cycles[i] or hulp[i]%40==cycles[i]-1 or hulp[i]%40==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    for i in range(80,120):
        if hulp[i]%40==cycles[i] or hulp[i]%40==cycles[i]-1 or hulp[i]%40==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    for i in range(120,160):
        if hulp[i]%40==cycles[i] or hulp[i]%40==cycles[i]-1 or hulp[i]%40==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    for i in range(160,200):
        if hulp[i]%40==cycles[i] or hulp[i]%40==cycles[i]-1 or hulp[i]%40==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    for i in range(200,240):
        if hulp[i]%40==cycles[i] or hulp[i]%40==cycles[i]-1 or hulp[i]%40==cycles[i]+1:
            output.append('#')
        else:
            output.append('.')
    print(output[20:40])
    print(output[60:80])
    print(output[100:120])
    print(output[140:160])
    print(output[180:200])
    print(output[220:240])
    #print (cycles[20],cycles[60],cycles[100],cycles[140],cycles[180],cycles[220])
    return cycles[20]*20+cycles[60]*60+cycles[100]*100+cycles[140]*140+cycles[180]*180+cycles[220]*220



    
    

    return None

        



start=pfc()
print(solve(read_puzzle('dag10.txt')))
print(pfc()-start)