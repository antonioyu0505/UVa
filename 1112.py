# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/28
# Antonio Yu
# ID: 8923359
# 1112 - Mice and Maze

from sys import stdin
from heapq import heappop, heappush

INF = float('inf')

def solve(G, source, time):
	dist = [INF for i in range(len(G))]
	dist[source] = 0
	visited = [False for i in range(len(G))]
	heap = [(0, source)]
	while(len(heap) != 0):
		d, u = heappop(heap)
		if(not visited[u]):
			visited[u] = True
			for v, w in G[u]:
				if(dist[v] > d + w):
					dist[v] = d + w
					heappush(heap, (dist[v], v))
	print(dist)
	return len([i for i in dist if i <= time])

def main():
	line = stdin.readline().strip()
	cases = int(line)
	while(cases != 0):
		line = stdin.readline().strip()
		D = [0 for _ in range(4)]
		for i in range(4):
			line = stdin.readline().strip()
			D[i] = int(line)
		G = [[] for _ in range(D[0])]
		for i in range(D[3]):
			line = stdin.readline().strip()
			a, b, w = [int(i) for i in line.split()]
			G[b - 1].append((a - 1, w))
		print(solve(G, D[1] - 1, D[2]))
		cases = cases - 1
		if(cases != 0): print()

main()