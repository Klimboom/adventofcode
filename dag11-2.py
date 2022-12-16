from time import perf_counter as pfc

help=2*3*5*7*11*13*17*19

mk=dict()
mk[0]=[85, 77, 77]
mk[1]=[80, 99]
mk[2]=[74, 60, 74, 63, 86, 92, 80]
mk[3]=[71, 58, 93, 65, 80, 68, 54, 71]
mk[4]=[97, 56, 79, 65, 58]
mk[5]=[77]
mk[6]=[99, 90, 84, 50]
mk[7]=[50, 66, 61, 92, 64, 78]

def monkey0(number):
    number=number%help
    number*=7
    #number//=3
    if number%19==0:
        mk[6].append(number)
    else:
        mk[7].append(number)

def monkey1(number):
    number=number%help
    number*=11
    #number//=3
    if number%3==0:
        mk[3].append(number)
    else:
        mk[5].append(number)

def monkey2(number):
    number=number%help
    number+=8
    #number//=3
    if number%13==0:
        mk[0].append(number)
    else:
        mk[6].append(number)

def monkey3(number):
    number=number%help
    number+=7
    #number//=3
    if number%7==0:
        mk[2].append(number)
    else:
        mk[4].append(number)

def monkey4(number):
    number=number%help
    number+=5
    #number//=3
    if number%5==0:
        mk[2].append(number)
    else:
        mk[0].append(number)

def monkey5(number):
    number=number%help
    number+=4
    #number//=3
    if number%11==0:
        mk[4].append(number)
    else:
        mk[3].append(number)

def monkey6(number):
    number=number%help
    number*=number
    #number//=3
    if number%17==0:
        mk[7].append(number)
    else:
        mk[1].append(number)

def monkey7(number):
    number=number%help
    number+=3
    #number//=3
    if number%2==0:
        mk[5].append(number)
    else:
        mk[1].append(number)

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test)
    return test


def solve(puzzle):
    zero=[0,0,0,0,0,0,0,0]

    print(mk)


    for r in range(10000):
        for i in range(len(mk)):
            if i==0:
                while len(mk[0])>0:
                    zero[i]+=1
                    monkey0(mk[0].pop(0))
            elif i==1:
                while len(mk[1])>0:
                    zero[i]+=1
                    monkey1(mk[1].pop(0))
            elif i==2:
                while len(mk[2])>0:
                    zero[i]+=1
                    monkey2(mk[2].pop(0))
            elif i==3:
                while len(mk[3])>0:
                    zero[i]+=1
                    monkey3(mk[3].pop(0))
            elif i==4:
                while len(mk[4])>0:
                    zero[i]+=1
                    monkey4(mk[4].pop(0))
            elif i==5:
                while len(mk[5])>0:
                    zero[i]+=1
                    monkey5(mk[5].pop(0))
            elif i==6:
                while len(mk[6])>0:
                    zero[i]+=1
                    monkey6(mk[6].pop(0))
            elif i==7:
                while len(mk[7])>0:
                    zero[i]+=1
                    monkey7(mk[7].pop(0))
        
            #print(r,mk,zero)
        
        
    zero=sorted(zero,reverse=True)
    return(zero[0]*zero[1])

start=pfc()
print(solve(read_puzzle('dag4.txt')))
print(pfc()-start)