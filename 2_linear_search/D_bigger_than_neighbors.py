li = [int(i) for i in input().split()]
if len(li) < 3:
    print(0)
else:
    count = 0
    for i in range(1, len(li) - 1):
        if li[i] > li[i - 1] and li[i] > li[i + 1]:
            count += 1
    print(count)