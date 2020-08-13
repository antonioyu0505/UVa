# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/22
# Antonio Yu
# ID: 8923359
# 11741 - Heavy Cycle Edges

from sys import stdin

class dforest(object):
	"""Disjoint-Union implementation with disjoint forests using
	path compression and ranking"""

	def __init__(self, size = 100):
		"""Create an empty disjoint forest"""
		self.__parent = [i for i in range(size)]
		self.__rank = [0 for _ in range(size)]

	def __str__(self):
		"""Return the string representation"""
		return str(self.__parent)

	def find(self, x):
		"""Return the representative of x"""
		if(self.__parent[x] != x): self.__parent[x] = self.find(self.__parent[x])
		return self.__parent[x]

	def union(self, x, y):
		"""Performs the union of the collections where x and y belong"""
		rx, ry = self.find(x), self.find(y)
		krx, kry = self.__rank[rx], self.__rank[ry]
		if(krx >= kry):
			self.__parent[ry] = rx
			if(krx == kry): self.__rank[rx] = self.__rank[rx] + 1
		else: self.__parent[rx] = ry

def kruskal(G, lenv):
	ans, ans2 = [], []
	G.sort(key = lambda x: x[2])
	df = dforest(lenv)
	for u, v, w in G:
		if(df.find(u) != df.find(v)):
			ans.append((u, v, w))
			df.union(u, v)
		else: ans2.append(w)
	return ans2

def main():
	line = stdin.readline().strip()
	while(line != '0 0'):
		n, m = [int(i) for i in line.split()]
		G = []
		line = stdin.readline().strip()
		for i in range(m):
			G.append([int(i) for i in line.split()])
			line = stdin.readline().strip()
		ans = kruskal(G, n)
		if(len(ans) > 0): print(" ".join(str(i) for i in ans))
		else: print("forest")
main()