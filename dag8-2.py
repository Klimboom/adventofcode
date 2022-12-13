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
    
    maxres=0
    
    for v in range(1,len(lines)-1):
        for h in range (1,len(lines[0])-1):  #buitenste overslaan
            res=1
            #naar links
            l=1
            while h-l>=0 and int(lines[v][h])>int(lines[v][h-l]):
                l+=1
            if h-l<0:
                l-=1

            res*=(l)
            #naar rechts
            r=1
            while h+r<(len(lines[0])) and int(lines[v][h])>int(lines[v][h+r]):
                r+=1
            if h+r==len(lines[0]):
                r-=1
            res*=(r)
            #omhoog
            o=1
            while v-o>=0 and int(lines[v][h])>int(lines[v-o][h]):
                o+=1
            if v-o<0:
                o-=1
            res*=(o)
            #omlaag
            d=1
            while v+d<(len(lines)) and int(lines[v][h])>int(lines[v+d][h]):
                d+=1
            if v+d==len(lines):
                d-=1
            res*=(d)
            
    
            maxres=max(res,maxres)

    return maxres

        



start=pfc()
print(solve(read_puzzle('dag8.txt')))
print(pfc()-start)