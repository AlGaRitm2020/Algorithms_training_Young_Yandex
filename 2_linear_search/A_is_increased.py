li = [int(i) for i in input().split()]
ans = "YES"
for i in range(1, len(li)):
    if li[i] <= li[i - 1]:
        ans = 'NO'
print(ans)
