# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/01
# Antonio Yu
# ID: 8923359
# 11413 - Fill the Containers

from sys import stdin

def fill(A, M, cap):
	currentCap = cap
	container = 1
	for i in range(len(A)):
		if(A[i] > cap): return False
		if(A[i] > currentCap):
			if(container == M): return False
			container = container + 1
			currentCap = cap
		currentCap = currentCap - A[i]
	return True

def solve(A, M):
	minCap, maxCap = 1, sum(A)
	while(minCap <= maxCap):
		mid = minCap + ((maxCap - minCap) >> 1)
		filled = fill(A, M, mid)
		if(filled): maxCap = mid - 1
		else: minCap = mid + 1
	print(minCap)

def main():
	line = stdin.readline()
	while len(line)!=0:
		n,M = [ int(x) for x in line.split() ]
		A = [ int(x) for x in stdin.readline().split() ]
		solve(A, M)
		line = stdin.readline()

main()
