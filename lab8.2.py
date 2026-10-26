n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range (n):
    max_index = a[i].index(max(a[i]))
    for j in range(max_index + 1, m):
        a[i][j] = 0
for i in range(n):
    print(*a[i])