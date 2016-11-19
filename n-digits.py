from sys import stdin
from random import randint

N, M = map(int, stdin.readline().strip().split())
for _ in range(M):
    print randint(10**N, 10**(N+1)-1) 
