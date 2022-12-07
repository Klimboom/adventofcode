from time import perf_counter as pfc

code='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def read_puzzle(file):
  with open(file) as f:
    return [line.strip() for line in f]


def solve(puzzle):
  #print (puzzle)
  gelijken=[]
  for line in puzzle:
    for letter in line[:len(line)//2]:
        #print(line[:len(line)//2])
        if letter in line[len(line)//2:]:
            gelijken.append(letter)
            break
  res=0
  print(gelijken)
  for letter in gelijken:
    res+=code.index(letter)+1
  print(res)


start=pfc()
print(solve(read_puzzle('Dag3.txt')))
print(pfc()-start)