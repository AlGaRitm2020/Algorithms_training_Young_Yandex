a, b, c = (int(input()) for _ in range(3))
# 0 0 0 +
# 0 0 1 +
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1

if c < 0:
    print('NO SOLUTION')
elif c == 0:
    if b == 0:
        if a == 0:
            print('MANY SOLUTIONS')
        else:
            print(0)
    elif a == 0:
        print('NO SOLUTION')
    else:
        result = (- b) / a
        if int(result) == result:
            print(int(result))
        else:
            print('NO SOLUTION')

else:
    if a == 0:
        if b == c ** 2:
            print('MANY SOLUTIONS')
        else:
            print('NO SOLUTION')
    else:
        result = (c ** 2 - b) / a
        if int(result) == result:
            print(int(result))
        else:
            print('NO SOLUTION')