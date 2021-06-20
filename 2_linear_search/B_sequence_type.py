li = [int(input())]
i = 0
while li[i] != -2 * 10 ** 9:
    li.append(int(input()))
    i += 1
del li[-1]

dict = {
    'CONSTANT': True,
    'ASCENDING': True,
    'WEAKLY_ASCENDING': True,
    'DESCENDING': True,
    'WEAKLY_DESCENDING': True
}

for i in range(1, len(li)):
    if li[i] != li[i - 1]:
        dict['CONSTANT'] = False
        if li[i] > li[i - 1]:
            dict['DESCENDING'] = False
            dict['WEAKLY_DESCENDING'] = False
        elif li[i] < li[i - 1]:
            dict['ASCENDING'] = False
            dict['WEAKLY_ASCENDING'] = False
    else:
        dict['DESCENDING'] = False
        dict['ASCENDING'] = False

if not li:
    pass
elif not any(dict.values()):
    print('RANDOM')
else:
    for key, value in dict.items():
        if value:
            print(key)
            break