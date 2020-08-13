# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 10077 - The Stern-Brocot Number System
# Colaboradores: https://en.wikipedia.org/wiki/Stern%E2%80%93Brocot_tree

from sys import stdin

def solve(q1, q2):
	L, R, ans = [0, 1], [1, 0], []
	M = [L[0] + R[0], L[1] + R[1]]
	while(M[0] != q1 or M[1] != q2):
		if(M[0] * q2 > M[1] * q1):
			R = M
			ans.append('L')
		else:
			L = M
			ans.append('R')
		M = [L[0] + R[0], L[1] + R[1]]
	print(''.join(ans))

def main():
	inp = stdin.readline().strip()
	while(inp != '1 1'):
		q1, q2 = [int(i) for i in inp.split()]
		solve(q1, q2)
		inp = stdin.readline().strip()

main()