# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/25
# Antonio Yu
# ID: 8923359
# 11561 - Getting Gold

from sys import stdin

dirPlayer = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs_iterative(G, P, n, m):
	"""-1 will be trap, 0 will be wall, 1 will be floor, 2 will be Gold, 3 will be Player."""
	stack = []
	visited = [[0 for _ in range(m)] for _ in range(n)]
	ans = 0
	flag = True
	for x, y in dirPlayer:
		xi, yi = x + P[0], y + P[1]
		if(0 <= xi < n and 0 <= yi < m and G[xi][yi] == -1): flag = False
	if(flag): stack.append(P)
	while(stack):
		u = stack.pop()
		for x, y in dirPlayer:
			xi, yi = x + u[0], y + u[1]
			flag = True
			if(0 <= xi < n and 0 <= yi < m and visited[xi][yi] != 1):
				if(G[xi][yi] == 2): ans = ans + 1
				if(G[xi][yi] == 1 or G[xi][yi] == 2):
					for x1, y1 in dirPlayer:
						x2, y2 = x1 + xi, y1 + yi
						if(0 <= x2 < n and 0 <= y2 < m and G[x2][y2] == -1): flag = False
					if(flag): 
						stack.append((xi, yi))
				visited[xi][yi] = 1
	print(ans)

def solve(M, n, m):
	G = [[0 for _ in range(m)] for _ in range(n)]
	P = None
	for i in range(n):
		flag = True
		for j in range(m):
			if(M[i][j] == 'T'): G[i][j] = -1
			elif(M[i][j] == '.'): G[i][j] = 1
			elif(M[i][j] == 'G'): G[i][j] = 2
			elif(M[i][j] == 'P'): 
				G[i][j] = 3
				P = (i, j)
	dfs_iterative(G, P, n, m)

def main():
	line = stdin.readline().strip()
	while(line != ''):
		m, n = [int(i) for i in line.split()]
		M = []
		for i in range(n):
			line = stdin.readline().strip()
			M.append(line)
		solve(M, n, m)
		line = stdin.readline().strip()
main()