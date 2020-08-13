# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 11003 - Boxes

from sys import stdin

def solve(W, L, M):
	N = len(W)
	tab = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
	n, m = 1, 0
	while(n != N + 1):
		if(m == M + 1): n, m = n + 1, 0
		else:
			tab[n][m] = tab[n - 1][m]
			if(W[n - 1] <= m):
				tab[n][m] = max(tab[n][m], 1 + tab[n - 1][min(m - W[n - 1], L[n - 1])])
			m = m + 1
	print(tab[N][M])


def main():
	inp = stdin.readline()
	while(inp.strip() != '0'):
		W, L, M = [], [], 0
		boxes = int(inp)
		inp = stdin.readline()
		for i in range(boxes):
			B = [int(i) for i in inp.split()]
			W.append(B[0])
			L.append(B[1])
			M = max(M, sum(B))
			inp = stdin.readline()
		W.reverse()
		L.reverse()
		solve(W, L, M)
main()
