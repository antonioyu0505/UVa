# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/01/31
# Antonio Yu
# ID: 8923359
# 10684 - The Jackpot

from sys import stdin

def solve(A):
  ans, n = [0 for i in range(len(A))], len(A)
  ans[0] = A[0]
  for i in range(1, n):
    ans[i] = ans[i - 1] + A[i]
    if(A[i] > ans[i]): ans[i] = A[i]
  return max(ans)

def main():
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): tok[i] = int(tok[i])
    ans = solve(tok)
    if ans<=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(ans))
    n = int(inp.readline().strip())

main()
