now, goal = (int(i) for i in input().split())
mode = input()
if mode == 'fan':
    print(now)
elif mode == 'auto':
    print(goal)
elif mode == 'freeze':
    if now > goal:
        print(goal)
    else:
        print(now)
else:
    if now < goal:
        print(goal)
    else:
        print(now)