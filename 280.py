# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/29
# Antonio Yu
# ID: 8923359
# 280 - Vertex

from sys import stdin
from collections import deque

def solve(G, source):
	visited = [False for _ in range(len(G))]
	queue = deque()
	queue.append(source)
	while(queue):
		u = queue.popleft()
		for v in G[u]:
			if(not visited[v]):
				visited[v] = True
				queue.append(v)
	return [i + 1 for i in range(len(visited)) if not visited[i]]

def main():
	line = stdin.readline().strip()
	while(line != '0'):
		N = int(line)
		G = [[] for _ in range(N)]
		line = stdin.readline().strip()
		while(line != '0'):
			E = [int(i) for i in line.split()]
			G[E[0] - 1].extend([E[i] - 1 for i in range(1, len(E) - 1)])
			line = stdin.readline().strip()
		line = stdin.readline().strip()
		C = [int(i) for i in line.split()]
		ans = []
		for i in range(C[0]): ans.append(solve(G, C[i + 1] - 1))
		for i in ans:
			N = len(i)
			print("{} {}".format(N, " ".join(str(j) for j in i)) if N != 0 else 0)
		line = stdin.readline().strip()
main()