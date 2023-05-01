tCase = int(input())
while tCase:
    food = float(input())
    days = 0
    while True:
        food = food / 2
        if food > 1:
            days += 1
        else:
            days += 1
            break
    print(days, 'days')
    tCase -= 1