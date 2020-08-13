# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/02/18
# Antonio Yu
# ID: 8923359
# 5226 - Making Change
# Colaboradores: Iván Valderrama, Juan Esteban Cardona

from sys import stdin

INF = float('inf')
coins = [1, 2, 4, 10, 20, 40]

def cc_tab_optimized(N, X):
	if(X == 0): return 0
	elif(sum(coins) == 0): return INF
	else:
		tab = [INF for _ in range(X + 1)]
		tab[0], n, x = 0, 1, 1
		while(n != N + 1):
			if(x == X + 1): x, n = 1, n + 1
			else:
				if(coins[n - 1] <= x):
					tab[x] = min(tab[x], 1 + tab[x - coins[n - 1]])
				x = x + 1
	return tab[len(tab) - 1]

def solve(C, x):
	ans = 0
	for i in range(len(C) - 1, -1, -1):
		if(C[i] != 0):
			if(coins[i] <= x):
				amount = min(x // coins[i], C[i])
				ans = ans + amount
				x = x - amount * coins[i]
	if(x != 0): ans = INF
	return ans

def main():
	global coins, INF
	inp = stdin.readline()
	coinsKeeper = {}
	for i in range(1, 41): coinsKeeper[i] = cc_tab_optimized(6, i)
	print(coinsKeeper)
	while(inp.strip() != "0 0 0 0 0 0"):
		q = inp.split()
		C, x = [int(q[i]) for i in range(len(q) - 1)], round(float(q[len(q) - 1]) * 100) // 5
		value = solve(C, x)
		for i in range(1, 41):
			value = min(value, solve(C, x + i) + coinsKeeper[i])
		print("%3d" % (value))
		inp = stdin.readline()
main()