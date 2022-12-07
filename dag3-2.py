from time import perf_counter as pfc

code='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test.split('\n'))
    return test.split('\n')


def solve(puzzle):
    begin=0
    gelijken=[]
    while begin<=len(puzzle)-3:
        for letter in puzzle[begin]:
            if letter in puzzle[begin+1] and letter in puzzle[begin+2]:
                gelijken.append(letter)
                break
        begin+=3
    print (gelijken)
    som=0
    for letter in gelijken:
        som+=code.index(letter)+1
    return som


start=pfc()
print(solve(read_puzzle('Dag3.txt')))
print(pfc()-start)