# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 437 - The Tower of Babylon

from sys import stdin
from itertools import permutations

MAX = 35

def solve(blocks):
	A = []
	for i in blocks:
		for j in permutations(i):
			A.append(j)
	A.sort(reverse = True)
	N = len(A)
	height = [i[2] for i in A]
	for i in range(N):
		for j in range(i):
			if(A[i][0] < A[j][0] and A[i][1] < A[j][1]):
				height[i] = max(height[i], A[i][2] + height[j])
	return max(height)

def main():
	n = int(stdin.readline().strip())
	case = 1
	while n!=0:
		blocks = []
		for i in range(n):
			x, y, z = map(int, stdin.readline().strip().split())
			blocks.append((x, y, z))
		ans = solve(blocks)
		print('Case {0}: maximum height = {1}'.format(case, ans))
		n = int(stdin.readline().strip())
		case += 1

main()
