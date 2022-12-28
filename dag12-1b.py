from time import perf_counter as pfc
import sys
from collections import deque



def findNeighbours(adjList,doolhof):

    for x in range(len(doolhof)): #rows
        for y in range(len(doolhof[0])): #cols
            #1.Up
            if canVisit(x-1, y ,x,y,doolhof):
                adjList[(x,y)].append((x-1,y))
            #2.Down
            if canVisit(x+1, y,x,y,doolhof):
                adjList[(x,y)].append((x+1,y))
  
            #3.Left
            if canVisit(x, y-1,x,y,doolhof):
                adjList[(x,y)].append((x,y-1))

            #4.Right
            if canVisit(x, y+1,x,y,doolhof):
                adjList[(x,y)].append((x,y+1))
    return adjList
 
  
  

  

#Function checks if (x,y) cell is valid cell or not
def canVisit(x, y,xold,yold,matrix):
  
  code=ord(matrix[xold][yold])-96
  if code<0:
    code=0
  #check maze boundaries
  if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]):
    return False
  if matrix[x][y]=='E' and matrix[xold][yold]=='z':
    return True
  #check alowed
  help=ord(matrix[x][y])-96
  #print(help)
  if help>code+1:
    return False
  
  return True



def read_puzzle(file):
    with open(file) as f:
        #return [sum(int(calories) for calories in elve.split('\n')) for elve in f.read().split('\n\n')]
        test=f.read()
    #print(test)
    return test

def findSE(puzzle):
    
    for i in range(len(puzzle)-1): #rows
        for j in range(len(puzzle[0])-1): #cols
            #print(puzzle[i][j])
            if puzzle[i][j]=='S':
                s=(i,j)
            if puzzle[i][j]=='E':
                e=(i,j)
    

    return s,e

def makeGraph(doolhof):
    graph={}
    for y in range(len(doolhof)): #rows
        for x in range(len(doolhof[0])): #cols
            #print (x,y)
            graph[(y,x)]=[]
    return graph


def bfs(graph,s,e):
    
    d = {s: 0}

    queue = deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        
        for n in graph[u]:
            if n not in d:
                d[n] = d[u] + 1
                queue.append(n)
    return d


def solve(puzzle):
    
    matrix=puzzle.split('\n')
    start,end=findSE(matrix)
    print(start,end)

    adj=makeGraph(matrix)
    #print(adj)

    adj=findNeighbours(adj,matrix)
    for key in adj.keys():
        if key[0]==20:
            print(key,adj[key])

    d=bfs(adj,start,end)
    print(d[(20,120)])
    
    

    return None
starttime=pfc()
print(solve(read_puzzle('dag12.txt')))
print(pfc()-starttime)