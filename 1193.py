# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/11
# Antonio Yu
# ID: 8923359
# 1193 - Radar Installation

from sys import stdin
from math import sqrt

def interval(Y, D):
	d = D * D - Y * Y
	if(d < 0): return -1
	return sqrt(d)

def solve(A):
	N = len(A)
	ans, n = 0, 0
	while(n != N):
		best, n = n, n + 1
		while(n != N and A[n][0] < A[best][1]):
			n = n + 1
		ans = ans + 1
	return ans

def main():
	line = stdin.readline().strip()
	case = 1
	while(line != '0 0'):
		N, D = [int(i) for i in line.split()]
		A, flag, n = [], True, 0
		line = stdin.readline().strip()
		while(n != N):
			x, y = [int(i) for i in line.split()]
			d = interval(y, D)
			flag = flag and d != -1
			A.append((x - d, x + d))
			n = n + 1
			line = stdin.readline().strip()
		line = stdin.readline().strip()
		A.sort(key = lambda a : a[1])
		ans = -1 if not flag else solve(A)
		print("Case {}: {}".format(case, ans))
		case = case + 1

main()