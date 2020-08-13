# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/25
# Antonio Yu
# ID: 8923359
# 1148 - The Mysterious X Network

from sys import stdin
from collections import deque

def bfs_iterative(G, c1, c2):
	visited = []
	distance = [float('inf') for _ in range(len(G))]
	distance[c1] = 0
	visited.append(c1)
	queue = deque()
	queue.append(c1)
	while(queue):
		u = queue.popleft()
		for v in G[u]:
			if(v not in visited):
				visited.append(v)
				distance[v] = distance[u] + 1
				queue.append(v)
	return distance[c2] - 1

def main():
	line = stdin.readline().strip()
	cases = int(line)
	line = stdin.readline().strip()
	while(cases != 0):
		line = stdin.readline().strip()
		case = int(line)
		G = [0 for _ in range(case)]
		line = stdin.readline().strip()
		for i in range(case):
			edges = [int(i) for i in line.split()]
			E = edges[2:]
			G[edges[0]] = E
			line = stdin.readline().strip()
		cases = cases - 1
		c1, c2 = [int(i) for i in line.split()]
		for i in G:
			print(i)
		ans = bfs_iterative(G, c1, c2)
		print("{} {} {}".format(c1, c2, ans))
		if(cases != 0): print()
		line = stdin.readline().strip()
main()