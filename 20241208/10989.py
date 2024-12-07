n = int(input())
m = [0]*10001
for i in range(n):
    a = int(input())
    m[a]+= 1
for i in range(len(m)):
    for j in range(m[i]):
        print(i)