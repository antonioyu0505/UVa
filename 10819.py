# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 10819 - Trouble of 13-Dots

from sys import stdin


# P is array of prices, F is array of favor, M is money available
def solve(P, F, M):
	N = len(P)
	tab = [[0 for _ in range(M + 201)] for _ in range(2)]
	n, m, flag = 1, M + 200, 1
	while(n != N + 1):
		if(m == 0): n, m, flag = n + 1, M + 200, not flag
		else:
			tab[flag][m] = tab[not flag][m]
			if(M + P[n - 1] - m > 2000 and m < P[n - 1] <= m + 200):
				tab[flag][m] = max(tab[flag][m], F[n - 1] + tab[not flag][m - P[n - 1] + 200])
			elif(P[n - 1] <= m):
				tab[flag][m] = max(tab[flag][m], F[n - 1] + tab[not flag][m - P[n - 1]])
			m = m - 1
	print(tab[not flag][M])

def main():
	inp = stdin.readline().strip()
	while(len(inp) != 0):
		M, N = [int(i) for i in inp.split()]
		P, F = [], []
		inp = stdin.readline().strip()
		for i in range(N):
			A = [int(i) for i in inp.split()]
			P.append(A[0])
			F.append(A[1])
			inp = stdin.readline().strip()
		solve(P, F, M)

main()