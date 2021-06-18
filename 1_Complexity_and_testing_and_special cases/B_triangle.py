a, b, c = (int(input()) for _ in range(3))
if a >= b + c:
    print('NO')
elif b >= a + c:
    print('NO')
elif c >= a + b:
    print('NO')
else:
    print('YES')