# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/25
# Antonio Yu
# ID: 8923359
# 11352 - Crazy King

from sys import stdin
from collections import deque

dirKing = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
dirKnight = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
INF = float('inf')

def bfs_iterative(G, A, B, n, m):
	"""If G[i][j] == 2, A is in that position, if G[i][j] == 3, B is in that position"""
	visited = [[0 for _ in range(m)] for _ in range(n)]
	distance = [[INF for _ in range(m)] for _ in range(n)]
	distance[A[0]][A[1]] = 0
	visited[A[0]][A[1]] = 1
	queue = deque()
	queue.append(A)
	while(queue):
		u = queue.popleft()
		for x, y in dirKing:
			xi, yi = x + u[0], y + u[1]
			if(0 <= xi < n and 0 <= yi < m and G[xi][yi] != 0 and visited[xi][yi] != 1):
				distance[xi][yi] = distance[u[0]][u[1]] + 1
				queue.append((xi, yi))
				visited[xi][yi] = 1
	return distance[B[0]][B[1]]

def solve(M, n, m):
	G = [[1 for _ in range(m)] for _ in range(n)]
	A, B = None, None
	for i in range(n):
		for j in range(m):
			if(M[i][j] == 'Z'):
				G[i][j] = 0
				for x, y in dirKnight:
					xi, yi = x + i, y + j
					if(0 <= xi < n and 0 <= yi < m and M[xi][yi] == '.'): G[xi][yi] = 0
			elif(M[i][j] == 'A'): 
				A = (i, j)
				G[i][j] = 2
			elif(M[i][j] == 'B'): 
				B = (i, j)
				G[i][j] = 3
	for i in G:
		print(i)
	# ans = bfs_iterative(G, A, B, n, m)
	# if(ans == INF): print("King Peter, you can't go now!")
	# else: print("Minimal possible length of a trip is {}".format(ans))

def main():
	line = stdin.readline().strip()
	cases = int(line)
	while(cases != 0):
		line = stdin.readline().strip()
		n, m = [int(i) for i in line.split()]
		M = []
		for i in range(n):
			line = stdin.readline().strip()
			M.append(line)
		cases = cases - 1
		solve(M, n, m)
main()