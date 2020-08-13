# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/05/XX
# Antonio Yu
# ID: 8923359
# 1649 - Binomial Coefficients
# The ncr function was extracted from https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
# Codigo de honor
# Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali
# me comprometo a seguir los más altos estándares de integridad académica.


import operator as op
from functools import reduce
from sys import stdin

hi = [0, 0, 44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 100, 87, 
78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54, 54, 54]
values = {}

def choose23(n, k):
	"""Function that returns the result of doing N combined K, 
	with K being either 2 or 3, and N an integer."""
	ans = 0
	if(k == 2): ans = (n * (n - 1)) >> 1
	elif(k == 3): ans = (n * (n - 1) * (n - 2)) // 6
	return ans

def ncr(n, r):
	"""Function that returns the result of doing N combined R, 
	with both N and R an integer."""
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer // denom

def binsearch(n, r, low, hi):
	"""Function that returns a tuple (bool, integer). If the first value is False,
	a number n was found in the depth N of Pascal's Triangle, with the given R column."""
	flag = True
	while(low + 1 < hi and flag):
		mid = low + ((hi - low) >> 1)
		val = choose23(mid, r)
		if(val < n): low = mid
		elif(val > n): hi = mid
		else: 
			hi = mid
			flag = False
	return (flag, hi)

def precalculate():
	"""Procedure that precalculates and memorizes every possible value from the 4th column 
	to the 30th column of Pascal's Triangle."""
	for i in range(4, len(hi)):
		for j in range(i, hi[i]):
			val = ncr(j, i)
			if(val not in values.keys()): values[val] = set()
			values[val].add((j, i))
			values[val].add((j, j - i))

def solve(N):
	"""Procedure that calculates if a given N is in the second and third column of
	Pascal's Triangle. Once this is done, it prints all the possible combinations that
	yields N in such triangle."""
	if(N not in values.keys()): values[N] = set()
	for i in range(2, 4): 
		val = binsearch(N, i, 0, min(N, hi[i]))
		if(not val[0]):
			values[N].add((val[1], i))
			values[N].add((val[1], val[1] - i))
	values[N].add((N, 1))
	values[N].add((N, N - 1))
	ans = sorted(values[N])
	print(len(ans))
	print(" ".join("(%s)" % ",".join(map(str, i)) for i in ans))

def main():
	line = stdin.readline().strip()
	cases = int(line)
	precalculate()
	for _ in range(cases):
		line = stdin.readline().strip()
		N = int(line)
		solve(N)
main()