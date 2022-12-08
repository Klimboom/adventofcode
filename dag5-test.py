from time import perf_counter as pfc

stacks=[['Z','N'],['M','C','D'],['P']]




def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test)
    return test

def move(hoeveel,van,naar):
    hoeveel=int(hoeveel)
    tweede=hoeveel
    van=int(van)-1
    naar=int(naar)-1
    help=[]
    while hoeveel>0:
        help.append(stacks[van].pop())
        print(help)
        hoeveel-=1
    #print(help)
    while tweede>0:
        stacks[naar].append(help.pop())
        print(stacks[naar],'tweede')
        tweede-=1

    
    print(stacks[naar])

def solve(puzzle):
    for regel in puzzle.split('\n'):
        if 'm' in regel:
            a=regel.split()
            print(a)
            move(a[1],a[3],a[5])
            print(a)
            
    print(stacks)
    res=''
    for stack in stacks:
        res+=stack.pop()
    return res

start=pfc()
print(solve(read_puzzle('dag5-test.txt')))
print(pfc()-start)