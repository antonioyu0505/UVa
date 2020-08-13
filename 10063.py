# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/04/XX
# Antonio Yu
# ID: 8923359
# 10063 - Knuth's Permutation

from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10000)

def solve(array):
	array.reverse()
	B = deque() ; B.append([])
	C = deque()
	A = [B, C]
	index = 0
	while(array):
		solver(A[index], A[not index], array.pop())
		index = not index
	while(A[index]):
		ans = A[index].popleft()
		print("".join(i for i in ans))

def solver(A, B, value):
	while(A):
		C = A.popleft()
		for i in range(len(C) + 1):
			temp = C[:]
			temp.insert(i, value)
			B.append(temp)
	return B

def main():
	line = stdin.readline().strip()
	while(len(line) != 0):
		perm = list(line)
		solve(perm)
		line = stdin.readline().strip()
		if(len(line) != 0): print()
main()