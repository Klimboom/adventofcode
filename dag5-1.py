from time import perf_counter as pfc

'''
[N]     [C]                 [Q]    
[W]     [J] [L]             [J] [V]
[F]     [N] [D]     [L]     [S] [W]
[R] [S] [F] [G]     [R]     [V] [Z]
[Z] [G] [Q] [C]     [W] [C] [F] [G]
[S] [Q] [V] [P] [S] [F] [D] [R] [S]
[M] [P] [R] [Z] [P] [D] [N] [N] [M]
[D] [W] [W] [F] [T] [H] [Z] [W] [R]
 1   2   3   4   5   6   7   8   9 '''

stacks=[['D','M','S','Z','R','F','W','N'],['W','P','Q','G','S'],['W','R','V','Q','F','N','J','C'],
        ['F','Z','P','C','G','D','L',],['T','P','S'],['H','D','F','W','R','L'],
        ['Z','N','D','C'],['W','N','R','F','V','S','J','Q'],['R','M','S','G','Z','W','V']]




def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    print(test)
    return test

def move(hoeveel,van,naar):
    hoeveel=int(hoeveel)
    van=int(van)-1
    naar=int(naar)-1
    while hoeveel>0:
        stacks[naar].append(stacks[van].pop())
        hoeveel-=1

def solve(puzzle):
    for regel in puzzle.split('\n'):
        if 'm' in regel:
            a=regel.split()
            move(a[1],a[3],a[5])
            print(a)
    print(stacks)
    res=''
    for stack in stacks:
        res+=stack.pop()
    return res

start=pfc()
print(solve(read_puzzle('dag5.txt')))
print(pfc()-start)