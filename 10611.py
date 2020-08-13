# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/01/31
# Antonio Yu
# ID: 8923359
# 10611 - The Playboy Chimp

from sys import stdin

def maxBisect(A, x):
	N, ans = len(A), A[0]
	if(N > 0):
		low, hi = 0, N
		while(low + 1 != hi):
			mid = low + ((hi - low) >> 1)
			if(A[mid] < x): low = mid
			else: hi = mid
		ans = A[low]
	if(ans < x): return ans
	return 'X'

def minBisect(A, x):
	N, ans = len(A), A[0]
	if(N > 0):
		low, hi = 0, N - 1
		while(low + 1 != hi):
			mid = low + ((hi - low) >> 1)
			if(A[mid] <= x): low = mid
			else: hi = mid
		ans = A[hi]
	if(ans > x): return ans
	return 'X'

def solve(ladies, x):
  print("{} {}".format(maxBisect(ladies, x), minBisect(ladies, x)))


def main():
  inp = stdin
  inp.readline()
  ladies = [int(x) for x in inp.readline().split()]
  inp.readline()
  queries = [int(x) for x in inp.readline().split()]
  for x in queries:
    solve(ladies, x)

main()
