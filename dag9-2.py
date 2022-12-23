from time import perf_counter as pfc

pos=set()
pos.add((0,0))

def raakt(h,t):
    if abs(h[0]-t[0])<=1 and abs(h[1]-t[1])<=1:
        return True
    return False

def schuif(h,t):
    x,y=0,0
    
    if h[0]-t[0]==2:
        
        x=1
        if h[1]-t[1]==1:
            y=1
        if h[1]-t[1]==-1:
            y=-1
    if h[0]-t[0]==-2:
        x=-1
        if h[1]-t[1]==1:
            y=1
        if h[1]-t[1]==-1:
            y=-1
    if h[1]-t[1]==2:
        y=1
        if h[0]-t[0]==1:
            x=1
        if h[0]-t[0]==-1:
            x=-1
    if h[1]-t[1]==-2:
        y=-1
        if h[0]-t[0]==1:
            x=1
        if h[0]-t[0]==-1:
            x=-1
    return x,y

def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test)
    return test







def solve(puzzle):
    H=[0,0]
    T=[[0,0] for i in range(9)]
    print(T)
    pos.add((T[8][0],T[8][1]))


    regels=puzzle.split('\n')
    for regel in regels:
        delen=regel.split(' ')
        for i in range(int(delen[1])):
            if delen[0]=='R':
                H[0]+=1
            if delen[0]=='L':
                H[0]-=1
            if delen[0]=='U':
                H[1]+=1
            if delen[0]=='D':
                H[1]-=1
            print(delen, H,T)
            if not raakt(H,T[0]):
                h,v=schuif(H,T[0])
                T[0][0]+=h
                T[0][1]+=v
                print("schuif",H,T)
                #pos.add((T[0],T[1]))
            for j in range(1,9):
                if not raakt(T[j-1],T[j]):
                    h,v=schuif(T[j-1],T[j])
                    T[j][0]+=h
                    T[j][1]+=v
                    pos.add((T[8][0],T[8][1]))
                    print("schuif",H,T)
    return len(pos)
                
        
        

start=pfc()
print(solve(read_puzzle('dag9.txt')))
print(pfc()-start)