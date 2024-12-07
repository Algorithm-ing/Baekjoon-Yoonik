N=int(input())
for n in sorted([*set(input() for _ in range(N))], key=lambda x:(len(x),x)): print(n)