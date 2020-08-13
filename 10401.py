# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/XX
# Antonio Yu
# ID: 8923359
# 10401 - Injured Queen Problem
# Colaboradores: Jhoan Lozano

from sys import stdin

def solver(A, N):
	if(N == 1): return 1
	else:
		tab = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
		for i in range(N):
			temp = [1 for _ in range(N + 1)]
			if(A[i] != -1):
				temp = [0 for _ in range(N + 1)]
				temp[A[i]] = 1
			temp[0] = 0
			tab[i + 1] = temp
		n, m, temp, actual = 2, 1, sum(tab[1]), sum(tab[2])
		while(n != N + 1):
			if(m == N + 1):
				temp = sum(tab[n])
				n, m = n + 1, 1
				if(n != N + 1): actual = sum(tab[n])
			else:
				col = tab[n - 1][m] + tab[n - 1][m - 1]
				if(m != N): col = col + tab[n - 1][m + 1]
				if(actual == 1):
					if(tab[n][m] == 1): 
						tab[n][m] = temp - col
						m = N
				else: tab[n][m] = temp - col
				m = m + 1
		return temp

def main():
	inp = stdin.readline()
	while(len(inp) != 0):
		A, N, flag = [], len(inp.strip()), True # N is currently the length of inp, excluding '\n'
		for i in inp.strip():
			if(i == '?'): A.append(-1)
			elif(ord('0') <= ord(i) <= ord('9')): A.append(int(i))
			else: A.append(10 + ord(i) - ord('A'))
		for i in range(N - 1):
			if(A[i] != - 1 and A[i] - 1 <= A[i + 1] <= A[i] + 1): flag = False
		if(flag): print(solver(A, N))
		else: print(0)
		inp = stdin.readline()
main()