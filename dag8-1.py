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
    res=0
    
    for v in range(1,len(lines)-1):
        for h in range (1,len(lines[0])-1):  #buitenste overslaan
            #naar links
            l=1
            while h-l>=0 and int(lines[v][h])>int(lines[v][h-l]):
                l+=1
            if h-l<0:
                res+=1
                continue
            #naar rechts
            r=1
            while h+r<(len(lines[0])) and int(lines[v][h])>int(lines[v][h+r]):
                r+=1
            if h+r==len(lines[0]):
                res+=1
                continue
            #omhoog
            o=1
            while v-o>=0 and int(lines[v][h])>int(lines[v-o][h]):
                o+=1
            if v-o<0:
                res+=1
                continue
            #omlaag
            d=1
            while v+d<(len(lines)) and int(lines[v][h])>int(lines[v+d][h]):
                d+=1
            if v+d==len(lines):
                res+=1
                continue
            
    res+=(2*len(lines[0])+2*len(lines)-4)

    return res

        



start=pfc()
print(solve(read_puzzle('dag8.txt')))
print(pfc()-start)