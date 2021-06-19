contacts = [input().replace('-', '').replace('(', '').replace(')', '')[-10:]for _ in range(3)]
new = input().replace('-', '').replace('(', '').replace(')', '')[-10:]
for phone in contacts:

    print(new, phone)
    if len(phone) == 7:
        phone = '495' + phone
    if new in phone:
        print('YES')
    else:
        print('NO')