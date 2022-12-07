from time import perf_counter as pfc



def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test)
    return test


def solve(puzzle):
    sum=0
    regels=puzzle.split('\n')
    for regel in regels:
        delen=regel.split(',')
        #print(delen)
        a=delen[0].split('-')
        b=delen[1].split('-')
        #print(a,b)
        
        if int(a[1])>=int(b[0]) and int(a[1])<=int(b[1]):
            sum+=1
            print (a,b,sum)
            
        elif int(a[0])>=int(b[0]) and int(a[0])<=int(b[1]):
                sum+=1
                print (a,b,sum)
        elif int(a[0])>=int(b[0]) and int(a[1])<=int(b[1]):
                sum+=1
                print (a,b,sum)
        elif int(a[0])<=int(b[0]) and int(a[1])>=int(b[1]):
                sum+=1
                print (a,b,sum)
                
    return sum

start=pfc()
print(solve(read_puzzle('dag4.txt')))
print(pfc()-start)