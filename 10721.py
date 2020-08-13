# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 10721 - Bar Codes
# Colaboradores: Juan Esteban Cardona

from sys import stdin

def solve(N, K, M):
	tab = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
	n, k = 1, 1
	while(n != N + 1):
		if(k == K + 1): n, k = n + 1, 1
		else:
			if(n == k or (k == 1 and n <= M)): tab[n][k] = 1
			else:
				ans = 0
				for i in range(1, M + 1): 
					if(n - i > 0): ans = ans + tab[n - i][k - 1]
				tab[n][k] = ans
			k = k + 1
	print(tab[N][K])

def main():
	inp = stdin.readline()
	while(len(inp) != 0):
		B = [int(i) for i in inp.split()]
		solve(B[0], B[1], B[2])
		inp = stdin.readline()
		
main()