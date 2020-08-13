# Pontificia Universidad Javeriana, Cali
# Analisis y Diseño de Algoritmos
# 2019/04/XX
# Antonio Yu
# ID: 8923359
# 574 - Sum It Up

from sys import stdin

solutions = []

def solve(array, target, temp, i, N, sol):
	if(temp == target): 
		if(sol not in solutions): solutions.append(sol)
	elif(i != N):
		while(i < N):
			if(temp + array[i] > target): i = i + 1
			else:
				ans = sol[:]
				ans.extend([array[i]])
				solve(array, target, temp + array[i], i + 1, N, ans)
				i = i + 1

def main():
	global solutions
	line = stdin.readline().strip()
	case = [int(i) for i in line.split()]
	while(case[1] != 0):
		array = case[2:len(case)]
		print("Sums of {}:".format(case[0]))
		solve(array, case[0], 0, 0, len(array), [])
		if(len(solutions) != 0):
			for i in solutions:
				print("+".join(str(j) for j in i))
		else: print("NONE")
		line = stdin.readline().strip()
		case = [int(i) for i in line.split()]
		solutions = []

main()