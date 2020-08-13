# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/04/XX
# Antonio Yu
# ID: 8923359
# 10276 - Hanoi Tower Troubles Again!

from sys import stdin
from math import sqrt
pegs = []

def solver(n2):
	for x in range(len(pegs), n2):
		peg = [0 for _ in range(x + 1)]
		peg[0] = 1
		n, m = 1, 2
		while(n != len(peg) + 1):
			flag, i = True, 0
			while(flag and i != n):
				j = int(sqrt(peg[i] + m))
				if(peg[i] + m == j * j):
					peg[i] = m
					flag = False
				i = i + 1
			if(flag):
				if(n != len(peg)): peg[n] = m
				n = n + 1
			m = m + 1
		pegs.append(max(peg))

def solve(n):
	if(n > len(pegs)):
		solver(n)
	return pegs[n - 1]

def main():
	solver(50)
	line = stdin.readline().strip()
	cases = int(line)
	for i in range(cases):
		line = stdin.readline().strip()
		n = int(line)
		print(solve(n))

main()