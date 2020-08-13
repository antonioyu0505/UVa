# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/03/09
# Antonio Yu
# ID: 8923359
# 12321 - Gas Stations

from sys import stdin

def solve(H, C):
	N = len(C)
	C.sort()
	ans, low, n, flag = 0, 0, 0, True
	while(low < H and n != N and flag):
		best, n = n, n + 1
		flag = C[best][0] <= low
		while(n != N and C[n][0] <= low and flag):
			if(C[best][1] < C[n][1]): best = n
			n = n + 1
		low = C[best][1]
		ans = ans + 1
	flag = flag and low >= H
	if(not flag): ans = -1
	return ans

def main():
	line = stdin.readline().strip()
	while(line != '0 0'):
		H, G = (int(i) for i in line.split())
		C = []
		for i in range(G):
			line = stdin.readline().strip()
			p, c = [int(i) for i in line.split()]
			C.append((p - c, p + c))
		ans = solve(H, C)
		if(ans != -1): print(G - ans)
		else: print(ans)
		line = stdin.readline().strip()
main()