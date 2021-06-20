n = int(input())
li = [int(i) for i in input().split()]
x = int(input())

ans = li[0]
for i in range(1, n):
    if abs(x - li[i]) < abs(x - ans):
        ans = li[i]

print(ans)